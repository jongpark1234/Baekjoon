def process(l, r):
    global numlist
    num = 0
    for i in range(l, r + 1):
        if numlist[i] == 1:
            num += 1
    if num & 2:
        return False
    while l < r and numlist[l] == numlist[r]:
        l += 1
        r -= 1
    while l <= r:
        if numlist[l] ^ numlist[l + 1] != 0:
            return False
        l += 2
    return True
for i in range(int(input())):
    n = int(input())
    numlist = list(map(int, input().split()))
    Sum = 0
    for j in range(n):
        Sum ^= numlist[j]
    if Sum == 0:
        print('Draw')
        continue
    if n == 1:
        print('First')
        continue
    if n % 2 == 0:
        print('First')
        continue
    m = 0
    for j in range(31)[::-1]:
        if ((Sum >> j) & 1) != 0:
            m = j
            break
    for j in range(n):
        numlist[j] = (numlist[j] >> m) & 1
    if numlist[0] == 1 and process(1, n - 1):
        print('First')
        continue
    if numlist[n - 1] == 1 and process(0, n - 2):
        print('First')
        continue
    print('Second')
