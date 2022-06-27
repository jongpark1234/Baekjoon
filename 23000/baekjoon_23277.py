from sys import stdin
from bisect import bisect_left, bisect_right
result = 0
def calc(seg, a, b):
    ret = 0
    left, right = 0, len(seg)
    while left < right:
        mid = left + right >> 1
        if seg[mid][1] <= a:
            left = mid + 1
        else:
            right = mid
    while left < len(seg):
        l, r, temp = seg[left]
        if l >= b:
            break
        x, y = max(l, a), min(r, b)
        if x < y:
            ret += (y - x) * temp
        left += 1
    return ret
def solve(m, x, seg):
    global result
    numset = set()
    numset.add(0); numset.add(m)
    seg1, seg2 = [], []
    for i in seg:
        numset.add(i[0])
        numset.add(i[1])
        if i[0] < i[1]:
            seg1.append((i[0], i[1], i[2]))
        else:
            seg2.append((i[1], i[0], i[2]))
    numset = list(sorted(numset))
    seg1.sort()
    seg2.sort()
    numlist1, numlist2, numlist3, numlist4 = [], [], [], []
    for i in numset:
        a = b = c = d = 0
        for j in seg1:
            if j[0] < i and j[1] >= i:
                a = j[2]
            if j[0] <= i and j[1] >= i + 1:
                c = j[2]
        for j in seg2:
            if j[0] < i and j[1] >= i:
                b = j[2]
            if j[0] <= i and j[1] >= i + 1:
                d = j[2]
        if not i:
            a = b = -1
        elif i == m:
            c = d = -1
        numlist1 += [a]
        numlist2 += [b]
        numlist3 += [c]
        numlist4 += [d]
    for i in numset:
        num1 = max(i, x + i + 1 >> 1)
        num2 = num1 * 2 - x - i
        if num1 <= m:
            v = calc(seg1, i, num1) + calc(seg2, num2, num1)
            result = max(result, v)
            if num1 < m:
                idx1 = bisect_right(numset, num1)
                idx2 = bisect_right(numset, num2)
                while num2 < num1 and num1 < m:
                    while numset[idx1] <= num1:
                        idx1 += 1
                    while numset[idx2] <= num2:
                        idx2 += 1
                    sidx = idx2 + (numset[idx2] <= num2 + 1)
                    steps = max(1, min(numset[idx1] - num1, numset[idx2] - num2 >> 1, num1 - num2, m - num1))
                    v += steps * (numlist1[idx1] + numlist2[idx1] - numlist2[idx2] - numlist2[sidx])
                    if v > result:
                        result = v
                    num1 += steps
                    num2 += steps * 2
        if i + x // 2 >= m:
            continue
        for j in numset:
            if i >= j:
                continue
            if (j - i) * 2 <= x:
                v = calc(seg1, i, j) + calc(seg2, i, j)
                num1 = i + (x + 1 >> 1)
                if num1 <= m:
                    num2 = j + (x & 1)
                    value = v + calc(seg1, j, num1) + calc(seg2, num2, num1)
                    result = max(result, value)
                    if calc(seg1, i, j + x - (j - i) * 2) + calc(seg2, i, j + x - (j - i) * 2) <= result:
                        num1 = m
                    if num1 < m:
                        idx1 = bisect_right(numset, num1)
                        idx2 = bisect_right(numset, num2)
                        while num1 < m and num2 < num1:
                            while numset[idx1] <= num1:
                                idx1 += 1
                            while numset[idx2] <= num2:
                                idx2 += 1
                            sidx = idx2 + (numset[idx2] <= num2 + 1)
                            steps = max(1, min(numset[idx1] - num1, (numset[idx2] - num2) // 2, num1 - num2, m - num1))
                            value += steps * (numlist1[idx1] + numlist2[idx1] - numlist2[idx2] - numlist2[sidx])
                            if value > result:
                                result = value
                            num1 += steps
                            num2 += steps * 2
            if x - (j - i) > -1:
                num1 = min(m, j + (x - (j - i)) // 2)
                num2 = i + x - ((num1 - j) * 2 + (j-i))
                if num2 >= i and num2 <= j:
                    value = calc(seg1, i, num1) + calc(seg2, i, num2) + calc(seg2, j, num1)
                    result = max(result, value)
                    if calc(seg1, i, num1) + calc(seg2, i, num1) <= result:
                        num2 = m
                    if num2 < m:
                        idx1 = bisect_right(numset, num2)
                        idx2 = bisect_left(numset, num1) - 1
                        while num2 + 2 <= j and num1 > j:
                            while numset[idx1] <= num2:
                                idx1 += 1
                            while numset[idx2] >= num1:
                                idx2 -= 1
                            sidx = idx1 + (numset[idx1] <= num2 + 1)
                            steps = max(1, min((numset[idx1] - num2) // 2, num1 - numset[idx2], num1 - j, (j - num2) // 2))
                            value += steps * (numlist2[idx1] + numlist2[sidx] - numlist3[idx2] - numlist4[idx2])
                            if value > result:
                                result = value
                            num1 -= steps
                            num2 += steps * 2
m, x, n = map(int, stdin.readline().split())
solve(m, x, seg := [tuple(map(int, stdin.readline().split())) for _ in range(n)])
solve(m, x, [(i[1], i[0], i[2]) for i in seg])
solve(m, x, [(m - i[0], m - i[1], i[2]) for i in seg])
solve(m, x, [(m - i[1], m - i[0], i[2]) for i in seg])
print(result)
