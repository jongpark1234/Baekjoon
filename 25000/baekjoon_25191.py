n = int(input())
a, b = map(int, input().split())
print(min(a // 2 + b, n))
