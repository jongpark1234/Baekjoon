a, b, c = map(int, input().split())
result = b - a
if result % c == 0:
    print(result // c)
else:
    print(result // c + 1)
