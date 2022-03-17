def even(numlist):
    result = []
    for i in numlist:
        if i % 2 == 0:
            result.append(i)
    return result
for _ in range(int(input())):
    s = even(list(map(int, input().split())))
    print(sum(s), min(s))
