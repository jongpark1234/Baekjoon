n = int(input())
print(sum(list(map(lambda x: 1 / (0.5 if x == '0' else int(x)), input().split()))))
