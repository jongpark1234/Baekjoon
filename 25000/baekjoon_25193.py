from math import ceil
n = int(input())
s = input()
food = n - s.count('C')
print(ceil((n - food) / (food + 1)))
