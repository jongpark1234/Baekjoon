from math import ceil
result = 0
n = int(input())
files = list(map(int, input().split()))
cluster = int(input())
for i in files:
    if i:
        result += ceil(i / cluster) * cluster
print(result)
