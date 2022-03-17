for i in range(int(input())):
    print(sorted([input().split() for _ in range(int(input()))], key = lambda x : (-int(x[0])))[0][1])
