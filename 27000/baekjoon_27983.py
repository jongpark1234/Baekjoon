n = int(input())
x = list(map(int, input().split()))
l = list(map(int, input().split()))
c = input().split()
for i in range(n):
    for j in range(i + 1, n):
        if abs(x[i] - x[j]) <= l[i] + l[j] and c[i] != c[j]:
            print('YES')
            print(i + 1, j + 1)
            break
    else:
        continue
    break
else:
    print('NO')
