import itertools
import sys
n = int(sys.stdin.readline())
operators = ['+', '-', '*', '//']
operator = []
numlist = []
number = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
for i, j in zip(operators, op):
    operator.extend([i] * j)
length = len(operator)
operator = list(itertools.permutations(operator, length))
for i in set(operator):
    temp = number[0]
    for x, y in zip(number[1:], i):
        if y == '//':
            if temp < 0:
                temp = - (abs(temp) // x)
            else:
                temp = temp // x
        else:
            temp = eval(str(temp) + y + str(x))
    numlist.append(temp)
print(max(numlist), min(numlist), sep='\n')