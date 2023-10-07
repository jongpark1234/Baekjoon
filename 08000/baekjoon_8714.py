n = int(input())
a = list(map(int, input().split()))
print(min(a.count(0), a.count(1)))
