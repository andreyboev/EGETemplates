"""
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней.
Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в кучу один камень, добавить два камня
или увеличить количество камней в куче в два раза. При этом нельзя повторять ход, который этот же игрок делал на предыдущем ходу.
Повторять чужие ходы и свои более старые ходы разрешается.
Чтобы делать ходы, у каждого игрока есть неограниченное количество камней.
Игра завершается, когда количество камней в куче становится не менее 21. Победителем считается игрок, сделавший последний ход,
то есть первым получивший кучу, в которой будет 21 или больше камней. В начальный момент в куче было S камней, 1 ⩽ S ⩽ 20.
Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
19:
Укажите наименьшее значение S, при котором Петя не может выиграть за один ход, но у Пети есть выигрышная стратегия, позволяющая ему выиграть вторым ходом.
20:
Укажите два значения S, при которых у Вани есть выигрышная стратегия, позволяющая ему выиграть вторым ходом при любой игре Пети,
но у Вани нет стратегии, которая позволяла бы ему гарантированно выиграть первым ходом.
21:
Найдите наибольшее значение S, при котором у Пети есть выигрышная стратегия, позволяющая ему выиграть третьим ходом при любой игре Вани,
но у Пети нет стратегии, которая позволяла бы ему гарантированно выиграть первым или вторым ходом.
Ответ:
19: 8
20: 6, 7
21: 5
"""


def game(heap, moves, step, p, v):
    if heap >= 21:
        return moves % 2 == step % 2
    if moves == step:
        return 0
    # Если ходит Петя
    if (moves + 1) % 2 != 0:
        if p == 1:
            result = [game(heap + 2, moves + 1, step, 2, v), game(heap * 2, moves + 1, step, 3, v)]
        elif p == 2:
            result = [game(heap + 1, moves + 1, step, 1, v), game(heap * 2, moves + 1, step, 3, v)]
        elif p == 3:
            result = [game(heap + 1, moves + 1, step, 1, v), game(heap + 2, moves + 1, step, 2, v)]
        else:
            result = [game(heap + 1, moves + 1, step, 1, v), game(heap + 2, moves + 1, step, 2, v), game(heap * 2, moves + 1, step, 3, v)]
    # Если ходит Вася
    else:
        if v == 1:
            result = [game(heap + 2, moves + 1, step, p, 2), game(heap * 2, moves + 1, step, p, 3)]
        elif v == 2:
            result = [game(heap + 1, moves + 1, step, p, 1), game(heap * 2, moves + 1, step, p, 3)]
        elif v == 3:
            result = [game(heap + 1, moves + 1, step, p, 1), game(heap + 2, moves + 1, step, p, 2)]
        else:
            result = [game(heap + 1, moves + 1, step, p, 1), game(heap + 2, moves + 1, step, p, 2), game(heap * 2, moves + 1, step, p, 3)]

    return any(result) if ((moves + 1) % 2 == step % 2) else all(result)


print(f'19: {min(s for s in range(1, 21) if not game(s, 0, 1, 0, 0) and game(s, 0, 3, 0, 0))}')
print(f'20: {[s for s in range(1, 21) if not game(s, 0, 2, 0, 0) and game(s, 0, 4, 0, 0)]}')
print(f'21: {max(s for s in range(1, 21) if game(s, 0, 5, 0, 0) and not game(s, 0, 1, 0, 0) and not game(s, 0, 3, 0, 0))}')
