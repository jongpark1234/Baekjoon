n = int(input())
count = 0
for i in range(1, n + 1):
    if i % sum([int(c) for c in str(i)]) == 0:
        count += 1
print(count)
