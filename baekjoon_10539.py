n = int(input())
b = list(map(int, input().split()))
a = [b[0]]
for i in range(1, n):
    a.append(b[i] * (i + 1) - sum(a))
print(*a)
