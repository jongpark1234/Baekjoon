from math import comb
print(comb(*map(lambda x: int(x) - 1, input().split())))
