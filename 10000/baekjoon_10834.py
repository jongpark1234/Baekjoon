dir = 0
result = 1
for _ in range(int(input())):
    a, b, f = map(int, input().split())
    result = result // a * b
    if f == 1:
        dir ^= 1
print(dir, result)
