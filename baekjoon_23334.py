print(*sorted([input().split() for _ in range(int(input()))], key = lambda x: (-int(x[0]), -int(x[1]), -int(x[2])))[0][3:])
