l = int(input())
d = int(input())
x = int(input())
numlist = [i for i in range(l, d + 1) if sum(map(int, str(i))) == x]
print(numlist[0], numlist[-1])
