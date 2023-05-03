from functools import reduce
n = int(input())
a = list(map(int, input().split()))
x = reduce(lambda x, y: x ^ y, a, 0)
print(str(max(*(x ^ i for i in a), x)) * 2)
