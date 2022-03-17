def mul(x): return x * 5
numlist = list(map(int, input().split()))
numlist = list(map(mul, numlist))
print(sum(numlist))