from sys import *
numlist = []
for _ in range(7):
    num = int(stdin.readline())
    if num % 2 != 0:
        numlist.append(num)
try:
    print(sum(numlist), min(numlist), sep='\n')
except:
    print(-1)
