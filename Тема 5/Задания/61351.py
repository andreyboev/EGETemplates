"""
Алгоритм получает на вход натуральное число N и строит по нему новое число R следующим образом.

1. Строится двоичная запись числа N.
2. В конец двоичной записи добавляются две цифры, соответствующие двоичной записи остатка от деления исходного числа на 3.
3. В конец двоичной записи числа, полученного на предыдущем шаге, добавляются три цифры, соответствующие двоичной записи остатка от деления этого числа на 5.
4. Результатом работы алгоритма становится десятичная запись полученного числа R.

Пример. Дано число N = 13. Алгоритм работает следующим образом:

1. Строим двоичную запись: 13 = 1101.
2. Остаток от деления 13 на 3 равен 1, добавляем к двоичной записи цифры 01, получаем 110101 = 53.
3. Остаток от деления 53 на 5 равен 3, добавляем к двоичной записи цифры 011, получаем 110101011 = 427.
4. Результат работы алгоритма R = 427.

Определите количество принадлежащих отрезку [1111111110; 1444444416] чисел, которые могут получиться в результате работы этого алгоритма.
"""

def f(n):
    b = bin(n)[2:]
    b += bin(n % 3)[2:].zfill(2)
    b += bin(int(b, 2) % 5)[2:].zfill(3)
    return int(b, 2)

for i in range(1, 100):
    res = f(i)
    print(i, res, res // i)

# [1111111110; 1444444416]

print((1444444416 - 1111111110) // 32)

count = 0
# 1111111147 - первое число слева, которое может получиться в алгоритме
x = 1111111147
# 1444444400 - последнее число справа, которое может получиться в алгоритме
while x <= 1444444400:
    count += 1
    x += 32

print(count)