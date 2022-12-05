n = int(input())
print(+(len([i for i in map(int, input().split()) if i & 1]) == n // 2 + n % 2))
