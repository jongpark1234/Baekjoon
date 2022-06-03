from math import ceil
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
print(sum([ceil(max(0, i - b) / c) + 1 for i in a]))
