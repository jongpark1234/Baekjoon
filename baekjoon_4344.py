c = int(input())
for i in range(c):
    n = list(map(int, input().split()))
    avg = (sum(n[1:])) / n[0]
    upper = 0
    for i in n[1:]:
        if (i > avg):
            upper += 1
    print("{:.3f}%".format(round((upper/n[0]) * 100, 3)))