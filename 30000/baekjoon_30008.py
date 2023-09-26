n, k = map(int, input().split())
print(*map(lambda x: sum(i < int(x) * 100 // n for i in [-1, 4, 11, 23, 40, 60, 77, 89, 96]), input().split()))
