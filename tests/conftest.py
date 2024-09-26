import os
from datetime import datetime

import pytest
import sqlite3

from matplotlib import pyplot as plt
from matplotlib.colors import Normalize, LinearSegmentedColormap

def create_new_db():
    connection = sqlite3.connect('result.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS test (
        date_time   DATETIME,
        task_number BIGINT,
        task_type   INTEGER,
        result      INTEGER
    )
    ''')
    connection.commit()
    connection.close()

def add_result(date_time, task_number, task_type, result):
    connection = sqlite3.connect('result.db')
    cursor = connection.cursor()
    cursor.execute('insert into test (date_time, task_number, task_type, result) values (?, ?, ?, ?)',
                   (date_time, task_number, task_type, result))
    connection.commit()
    connection.close()

def update_result(date_time, task_number, task_type, result):
    connection = sqlite3.connect('result.db')
    cursor = connection.cursor()
    cursor.execute('update test set date_time = ?, result = ? where task_type = ? and task_number = ?',
                   (date_time, result, task_type, task_number))
    connection.commit()
    connection.close()

def get_result(task_number, task_type):
    connection = sqlite3.connect('result.db')
    cursor = connection.cursor()
    cursor.execute('select * from test where task_number = ? and task_type = ?',
                   (task_number, task_type))
    result = cursor.fetchone()
    connection.commit()
    connection.close()
    return result

def get_results():
    connection = sqlite3.connect('result.db')
    cursor = connection.cursor()
    cursor.execute('select * from test')
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

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
    for result in session.results.values():
        _, type, task = result.nodeid.split('::')
        type = int(type.split('_')[1])
        task = int(task.split('_')[1])
        old_solution = None
        if (type, task) in session.old_results:
            old_solution = get_result(task, type)
        if (session.old_results.count((type, task)) == 0 or
                (old_solution is not None and abs((datetime.fromtimestamp(old_solution[0] / 1000) - datetime.now()).days) >= 14)):
            if old_solution is not None:
                update_result(datetime.now(), task, type, 1 if result.passed else 0)
            else:
                add_result(datetime.now(), task, type, 1 if result.passed else 0)
    results = get_results()
    # тип, правильно, неправильно, всего, результат
    types = [[i + 1, 0, 0, 0, 0] for i in range(27)]
    for item in session.items:
        _, type, task = item.nodeid.split('::')
        type = int(type.split('_')[1])
        types[type - 1][3] += 1
    # date_time, task_number, task_type, result
    for res in results:
        types[res[2] - 1][1] += 1 if res[3] == 1 else 0
        types[res[2] - 1][2] += 1 if res[3] == 0 else 0

    for t in types:
        if t[3] > 0:
            t[4] = (100 - ((t[2] + t[3] - t[1]) / t[3]) * 100)

    t = [i + 1 for i in range(27)]
    values = [item[4] for item in types]

    norm = Normalize(vmin=-10, vmax=100)
    cmap = LinearSegmentedColormap.from_list("red_green", ["red", "yellow", "green"])
    colors = cmap(norm(values))

    plt.bar(t, values, width=1.1, color=colors)
    plt.xlabel('Тип задания')
    plt.ylabel('Значение')
    plt.title('Уровень подготовки')
    plt.xticks(t)
    plt.show()