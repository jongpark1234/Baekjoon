numlist1, numlist2 = [1], [1]
a = input()
b = input()
for i in a:
    if i == '1':
        numlist1.append(0)
    if i == '2':
        numlist1.append(1)
    if i == 'L':
        numlist1[-1] -= 1
    if i == 'R':
        numlist1[-1] += 1
    if i == 'U':
        r = numlist1.pop()
        if r >= 0:
            numlist1[-1] += r // 2
        else:
            numlist1[-1] += r // 2
            r -= r
            while r < 0:
                numlist1[-1] -= 1
                r += 2
for i in b:
    if i == '1':
        numlist2.append(0)
    if i == '2':
        numlist2.append(1)
    if i == 'L':
        numlist2[-1] -= 1
    if i == 'R':
        numlist2[-1] += 1
    if i == 'U':
        r = numlist2.pop()
        if r >= 0:
            numlist2[-1] += r // 2
        else:
            numlist2[-1] += r // 2
            r -= r
            while r < 0:
                numlist2[-1] -= 1
                r += 2
for i in range(len(numlist1))[::-1]:
    r = numlist1[i]
    if r >= 0:
        numlist1[i - 1] += numlist1[i] // 2
        numlist1[i] %= 2
    else:
        numlist1[i - 1] += numlist1[i] // 2
        numlist1[i] -= numlist1[i] // 2 * 2
        while numlist1[i] < 0:
            numlist1[i - 1] -= 1
            numlist1[i] += 2
for i in range(len(numlist2))[::-1]:
    r = numlist2[i]
    if r >= 0:
        numlist2[i - 1] += numlist2[i] // 2
        numlist2[i] %= 2
    else:
        numlist2[i - 1] += numlist2[i] // 2
        numlist2[i] -= numlist2[i] // 2 * 2
        while numlist2[i] < 0:
            numlist2[i - 1] -= 1
            numlist2[i] += 2
result = length = len(numlist1) + len(numlist2)
dist = i = 0
while i < len(numlist1) and i < len(numlist2) and abs(dist) < 10000000:
    dist <<= 1
    dist += numlist2[i] - numlist1[i]
    length -= 2
    result = min(result, length + abs(dist))
    i += 1
print(result)
