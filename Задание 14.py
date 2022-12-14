'''
Значение арифметического выражения

3·4^38 + 2·4^23 + 4^20 + 3·4^5 + 2·4^4 + 1

записали в системе счисления с основанием 16. Сколько значащих нулей содержится в этой записи?

Ответ: 15
'''

n = 3 * 4 ** 38 + 2 * 4 ** 23 + 4 ** 20 + 3 * 4 ** 5 + 2 * 4 ** 4 + 1
count = 0
while n > 0:
    if n % 16 == 0:
        count += 1
    n = n // 16
print(count)
