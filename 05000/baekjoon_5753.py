while True:
    n, d = map(int, input().split())
    if n == d == 0:
        break
    dinnerTable = [list(map(int, input().split())) for _ in range(d)]
    print('yes' if any(all(dinnerTable[j][i] for j in range(d)) for i in range(n)) else 'no')
