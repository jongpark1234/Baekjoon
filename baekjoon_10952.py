n = 0
numlist = []

while (True):
    a, b = map(int, input().split())
    if (a == 0 and b == 0):
        break
    numlist.append(a + b)
    n += 1    

for i in range(n):
    print(numlist[i])