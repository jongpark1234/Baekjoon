from math import ceil
s = int(input())
a = int(input())
b = int(input())
if s - a < 1:
    print(250)
else:
    print(ceil((s - a) / b) * 100 + 250)
