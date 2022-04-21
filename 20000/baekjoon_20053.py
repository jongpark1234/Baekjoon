A = lambda x:f'{min(x)} {max(x)}'
for _ in range(int(input())):
    input()
    print(A([*map(int, input().split())]))
