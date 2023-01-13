temp = 0
result = -float('inf')
n = int(input())
numlist1 = [tuple(map(int, input().split())) for _ in range(n)]
Sum = sum(map(lambda x: x[0], numlist1))
numlist2 = sorted([(Sum - numlist1[i][0] - numlist1[i][1], i) for i in range(n)])
for i in numlist2:
    result = max(result, i[0] - temp)
    temp += numlist1[i[1]][0]
print(result)
