n = int(input())
a = sorted(list(map(int, input().split())))
Sum = [0]
weather = False
for i in range(1, n + 1):
    Sum.append(Sum[i - 1] + a[i - 1])
for i in range(n + 1):
    for j in range(i):
        if (Sum[i] - Sum[j] - 4) % 7 == 0:
            print('YES')
            exit(0)
print('NO')
