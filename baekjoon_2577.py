a = int(input())
b = int(input())
c = int(input())
numlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
temp = str(a * b * c)
for i in range(len(temp)):
    numlist[int(temp[i])] += 1
for j in range(10):
    print(numlist[j])