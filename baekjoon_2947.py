numlist = list(input().split())
while numlist != sorted(numlist):
    for i in range(len(numlist) - 1):
        if numlist[i] > numlist[i + 1]:
            numlist[i], numlist[i + 1] = numlist[i + 1], numlist[i]
            print(' '.join(numlist))
