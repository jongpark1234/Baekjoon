n = int(input())
print(sum(min(i, n) for i in list(map(int, input().split()))))
