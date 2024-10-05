import os
import re
from datetime import datetime

import pytest
import sqlite3

from matplotlib import pyplot as plt, patches
from matplotlib.colors import Normalize, LinearSegmentedColormap
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


def create_new_db():
    with sqlite3.connect('result.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS test (
            date_time   DATETIME,
            task_number BIGINT,
            task_type   INTEGER,
            result      INTEGER
        )
        ''')

def add_result(date_time, task_number, task_type, result):
    with sqlite3.connect('result.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO test (date_time, task_number, task_type, result) VALUES (?, ?, ?, ?)',
                       (date_time, task_number, task_type, result))

def update_result(date_time, task_number, task_type, result):
    with sqlite3.connect('result.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE test SET date_time = ?, result = ? WHERE task_type = ? AND task_number = ?',
                       (date_time, result, task_type, task_number))

def get_result(task_number, task_type):
    with sqlite3.connect('result.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM test WHERE task_number = ? AND task_type = ?',
                       (task_number, task_type))
        return cursor.fetchone()

def get_results():
    with sqlite3.connect('result.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM test')
        return cursor.fetchall()

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

def show_available_task(tasks: list):
    square_size = 1   # Размер квадрата
    spacing = 0.2     # Промежуток между квадратами
    columns = 10      # Количество значений в строке
    fig, ax = plt.subplots()
    for i, value in enumerate(tasks):
        x = (i % columns) * (square_size + spacing)
        y = -(i // columns) * (square_size + spacing)
        square = plt.Rectangle((x, y), square_size, square_size, facecolor='blue', edgecolor='black')
        ax.add_patch(square)
        ax.text(x + square_size / 2, y + square_size / 2, str(value), ha='center', va='center', color='white')
    ax.set_xlim(0, columns * (square_size + spacing) - spacing)
    ax.set_ylim(-((len(tasks) // columns) + 1) * (square_size + spacing), square_size + 0.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Задания, доступные для исправления')
    return fig

def show_task_results(current_passed, current_failed):
    fig, ax = plt.subplots(figsize=(10, 3))
    for i, (task_type, task_number) in enumerate(current_passed):
        rect = patches.Rectangle((i, 1), 1, 1, linewidth=1, edgecolor='green', facecolor='lightgreen')
        ax.add_patch(rect)
        ax.text(i + 0.5, 1.5, f'{task_type}-{task_number}', ha='center', va='center', color='black')
    for i, (task_type, task_number) in enumerate(current_failed):
        rect = patches.Rectangle((i, 0), 1, 1, linewidth=1, edgecolor='red', facecolor='lightcoral')
        ax.add_patch(rect)
        ax.text(i + 0.5, 0.5, f'{task_type}-{task_number}', ha='center', va='center', color='black')
    ax.set_xlim(0, max(len(current_passed), len(current_failed)))
    ax.set_ylim(-0.5, 2)
    ax.set_xticks([])
    ax.set_yticks([0.5, 1.5])
    ax.set_yticklabels(['Неправильно', 'Правильно'])
    ax.set_title('Результаты текущей сессии')
    return fig

def plot_preparation_level(types):
    t = [i + 1 for i in range(27)]
    values = [item[4] for item in types]
    norm = Normalize(vmin=0, vmax=100)
    cmap = LinearSegmentedColormap.from_list("red_green", ["red", "orange", "green"])
    colors = cmap(norm(values))
    fig, ax = plt.subplots(figsize=(12, 5))
    bars = ax.bar(t, values, width=0.8, color=colors)
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval / 2, round(yval, 2),
                ha='center', va='center')
    ax.set_xlabel('Тип задания')
    ax.set_ylabel('Значение')
    ax.set_title('Уровень подготовки')
    ax.set_xticks(t)
    return fig

def extract_test_info(test_string):
    pattern = r'test_scripts\[(\d+)-[a-f0-9]+-TestType_(\d+)\]'
    match = re.search(pattern, test_string)
    if match:
        test_number = match.group(1)
        test_type = match.group(2)
        return int(test_type), int(test_number)
    else:
        return None, None

@pytest.hookimpl()
def pytest_sessionstart(session):
    if not os.path.exists('result.db'):
        create_new_db()
    old_results = [(res[2], res[1]) for res in get_results()]
    session.old_results = old_results
    session.results = dict()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == 'call':
        item.session.results[item] = result

@pytest.hookimpl()
def pytest_sessionfinish(session, exitstatus):
    current_passed = []
    current_failed = []
    now = datetime.now()
    for result in filter(lambda r: r.outcome != 'skipped', session.results.values()):
        type, task = extract_test_info(result.nodeid)
        old_solution = None
        if (type, task) in session.old_results:
            old_solution = get_result(task, type)
        # Если ранее данное задание не решалось или пришло время перерешивания
        if (session.old_results.count((type, task)) == 0 or
                (old_solution is not None and abs((datetime.fromtimestamp(old_solution[0]) - datetime.now()).days) >= 14)):
            # Если решение есть в БД
            if old_solution is not None:
                update_result(now.timestamp(), task, type, 1 if result.passed else 0)
            else:
                task_path = f'../Тема {type}/Задания/Задание {task}.py'
                if not result.passed and os.path.exists(task_path):
                    os.rename(task_path, f'../Тема {type}/Задания/-Задание {task}.py')
                add_result(now.timestamp(), task, type, 1 if result.passed else 0)
            if result.passed:
                current_passed.append((type, task))
            else:
                current_failed.append((type, task))
    results = get_results()
    # тип, правильно, неправильно, всего, результат
    #  0       1           2         3        4
    types = [[i + 1, 0, 0, 0, 0] for i in range(27)]
    for item in session.items:
        type, task = extract_test_info(item.nodeid)
        types[type - 1][3] += 1
    # date_time, task_number, task_type, result
    available_task = []
    for res in results:
        if abs((datetime.fromtimestamp(res[0]) - now).days) >= 14:
            available_task.append(f'{res[2]}.{res[1]}')
        types[res[2] - 1][1] += 1 if res[3] == 1 else 0
        types[res[2] - 1][2] += 1 if res[3] == 0 else 0

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 16))

    available_task_fig = show_available_task(available_task)
    available_task_canvas = FigureCanvas(available_task_fig)
    available_task_canvas.draw()
    available_task_rgba_buffer = available_task_canvas.buffer_rgba()
    ax3.imshow(available_task_rgba_buffer, aspect='equal')
    ax3.axis('off')

    for t in types:
        if t[3] > 0:
            t[4] = clamp((100 - ((t[2] + t[3] - t[1]) / t[3]) * 100), 0, 100)

    task_results_fig = show_task_results(current_passed, current_failed)
    task_results_canvas = FigureCanvas(task_results_fig)
    task_results_canvas.draw()
    task_results_rgba_buffer = task_results_canvas.buffer_rgba()
    ax1.imshow(task_results_rgba_buffer, aspect='equal')
    ax1.axis('off')

    preparation_level_fig = plot_preparation_level(types)
    preparation_level_canvas = FigureCanvas(preparation_level_fig)
    preparation_level_canvas.draw()
    preparation_level_rgba_buffer = preparation_level_canvas.buffer_rgba()
    ax2.imshow(preparation_level_rgba_buffer, aspect='equal')
    ax2.axis('off')

    fig.tight_layout()
    fig.show()
