from itertools import permutations

table = '13 14 16 25 27 31 34 35 41 43 45 46 47 52 53 54 61 64 67 72 74 76'
graph = 'AB BA AG GA GF FG FE EF ED DE DB BD BC CB CD DC CE EC CF FC CG GC'

print('1 2 3 4 5 6 7')
for p in permutations('ABCDEFG'):
    new_graph = table
    for i in range(1, 8):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(' '.join(p))
