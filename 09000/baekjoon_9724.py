from sys import stdin
from math import ceil
for i in range(int(input())):
    a, b = map(lambda x: ceil(int(x) ** (1/3)), stdin.readline().split())
    print(f'Case #{i + 1}: {b - a}')
