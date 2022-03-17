n, d = map(int, input().split())
frequency = [0] * 10
numlist = [str(i) for i in range(1, n + 1)]
for i in numlist:
    for j in range(len(i)):
        frequency[int(i[j])] += 1
print(frequency[d])
