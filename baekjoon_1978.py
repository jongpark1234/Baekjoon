n = int(input())
numlist = list(map(int, input().split()))
count = 0
for i in numlist:
    wrong = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                wrong += 1
        if wrong == 0:
            count += 1
print(count)