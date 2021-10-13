n = int(input())
temp = 0
for i in range(1, n + 1):
    if i <= 99:
        temp += 1
    else:
        numlist = list(map(int, str(i)))
        if numlist[0] - numlist[1] == numlist[1] - numlist[2]:
            temp += 1
print(temp)