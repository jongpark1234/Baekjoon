n = int(input()); numlist = list(map(int, input().split())); v = int(input()); count = 0
for i in numlist:
    if v == i: count += 1
print(count)
