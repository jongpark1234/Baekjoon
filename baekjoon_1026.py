temp = 0
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort(), b.sort(), b.reverse()
for i in range(n):
    temp += a[i] * b[i]
print(temp)
