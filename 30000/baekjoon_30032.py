alDict = {
    'd': 'qb',
    'b': 'pd',
    'q': 'dp',
    'p': 'bq'
}
n, d = map(int, input().split())
for _ in range(n):
    print(''.join(map(lambda x: alDict[x][d - 1], input())))
