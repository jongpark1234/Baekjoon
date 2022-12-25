from math import prod
for _ in range(int(input())):
    print(f'${prod(list(map(float, input().split()))):.2f}')
