r, c = map(int, input().split())
a, b = map(int, input().split())
for R in range(r):
    for i in range(a):
        for C in range(c):
            for j in range(b):
                print('X' if R % 2 == C % 2 else '.', end='')
        print()
