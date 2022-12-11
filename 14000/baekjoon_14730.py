from math import prod
print(sum(prod([*map(int, input().split())]) for _ in range(int(input()))))
