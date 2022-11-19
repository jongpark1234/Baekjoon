n, m = map(int, input().split())
x = list(map(int, input().split()))
print(max([x.count(i) for i in range(max(x) + 1)]))
