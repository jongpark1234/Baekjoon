n = int(input())

for i in range(n):
    t = list(map(int, input().split()))
    print(t)
    print("{:.3f}".format(round((2/5) * 100, 4)))