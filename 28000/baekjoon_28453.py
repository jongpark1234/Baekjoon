input()
print(*map(lambda x: (x < 250) + (x < 275) + (x < 300) + 1, map(int, input().split())))
