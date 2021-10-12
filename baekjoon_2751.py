from sys import *
numlist = []
n = int(stdin.readline())
for i in range(n):
    numlist.append(int(stdin.readline()))
numlist.sort()
for j in range(n):
    print(numlist[j])