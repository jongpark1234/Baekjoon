n = int(input())
a = list(map(int, input().split()))
x, y = map(int, input().split())
print(int(n * x / 100), len([i for i in a if i >= y]))
