n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(sum(max(a[i] - b[i], 0) for i in range(n)))
