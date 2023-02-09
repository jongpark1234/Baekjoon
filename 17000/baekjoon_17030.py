result = -float('inf')
l = r = 0
prodValue, sumValue = 1, 0
n = int(input())
numlist = [int(input()) * 0.000001 for _ in range(n)]
while l < n:
    while r < n and sumValue < 1:
        prodValue *= 1 - numlist[r]
        sumValue += numlist[r] / (1 - numlist[r])
        r += 1
    result = max(result, prodValue * sumValue)
    prodValue /= 1 - numlist[l]
    sumValue -= numlist[l] / (1 - numlist[l])
    l += 1
print(int(result * 1000000))
