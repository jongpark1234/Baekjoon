def rKey(numlist):
    for i in range(n)[::-1]:
        if numlist[keyboards[i]]:
            numlist[keyboards[i]] = False
            return numlist
def rFor(numlist):
    for i in range(n)[::-1]:
        if numlist[formats[i]]:
            numlist[formats[i]] = False
            return numlist
def solve1(numlist):
    Sum = sum(numlist)
    for i in range(Sum - 1):
        numlist = rFor(numlist[:]) if i & 1 else rKey(numlist[:])
    return numlist.index(True)
def solve2(numlist):
    Sum = sum(numlist)
    if Sum > 1 and Sum & 1:
        ret = formats[-1]
        for i in range(n):
            if numlist[i]:
                numlist[i] = False
                idx = solve1(numlist)
                if s2[idx] < s2[ret]:
                    ret = idx
                numlist[i] = True
        return ret
    for i in range(Sum - 1):
        numlist = rKey(numlist[:]) if i & 1 else rFor(numlist[:])
    return numlist.index(True)
n = int(input())
keyboards, formats, ways = [], [], []
s1, s2 = [0 for _ in range(n)], [0 for _ in range(n)]
Input = list(map(lambda x: int(x) - 1, input().split()))
for i in range(n):
    keyboards.append(Input[i])
    s1[keyboards[i]] = i
Input = list(map(lambda x: int(x) - 1, input().split()))
for i in range(n):
    formats.append(Input[i])
    s2[formats[i]] = i
chosen = keyboards[-1]
for i in range(n):
    idx = solve2([True for _ in range(i)] + [False] + [True for _ in range(n - i - 1)])
    if s1[idx] < s1[chosen]:
        ways.clear()
        chosen = idx
    if s1[idx] == s1[chosen]:
        ways.append(i)
print(chosen + 1)
print(len(ways))
print(*map(lambda x: x + 1, ways))
