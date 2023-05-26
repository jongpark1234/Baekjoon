n = int(input())
print(max([i - (n - idx) for idx, i in enumerate(map(int, input().split()))]))
