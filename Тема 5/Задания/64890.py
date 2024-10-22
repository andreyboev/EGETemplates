def f(n):
    b = bin(n)[2:]
    b += bin(n % 4)[2:]
    return int(b, 2)


for i in range(894728061 - 100, 894728061 + 1):
    res = f(i)
    print(i, res, res // i)

# [1000000000; 1789456123]
'''
TODO: Дорешать!
'''
x = 1000000000
count = 0
while x <= 1789456123:
    count += 2
    x += 2
print(count)
