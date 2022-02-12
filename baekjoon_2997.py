numlist = sorted(list(map(int, input().split())))
if numlist[1] - numlist[0] == numlist[2] - numlist[1]:
    print(numlist[2] * 2 - numlist[1])
elif numlist[1] - numlist[0] > numlist[2] - numlist[1]:
    print(numlist[1] * 2 - numlist[2])
else:
    print(numlist[1] * 2 - numlist[0])
