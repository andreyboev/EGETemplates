for n in range(100):
    b = bin(n)[2:]
    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)
    res = int(b, 2)
    if res > 154:
        print(n)
        break