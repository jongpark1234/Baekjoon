from sys import *
a = int(stdin.readline())
b = int(stdin.readline())
c = int(stdin.readline())
d = int(stdin.readline())
p = int(stdin.readline())
x = a * p
if (p <= c):
    y = b
else:
    y = (p - c) * d + b
if (x <= y):
    print(x)
else:
    print(y)
