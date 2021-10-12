n = int(input())
upper = 0
temp = 0
for i in range(n):
    t = list(map(int, input().split()))
    temp = (sum(t) - t[0]) / t[0]
    i = 1
    for i in range(t[1:]):
        if (t[i] > temp):
            upper += 1
    print("{:.3f}%".format(round((upper/t[0]) * 100, 4)))
    upper = 0