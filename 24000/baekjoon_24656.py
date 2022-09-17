result = 0
for _ in range(int(input())):
    temp = 0
    a, b = map(int, input().split())
    if b & 1:
        temp = a & 1
    else:
        a %= b + 1
        temp = 2 if a == b else a & 1
    result ^= temp
print('Alice' if result else 'Bob')
