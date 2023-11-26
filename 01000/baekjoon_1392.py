n, q = map(int, input().split())
musiclist = [int(input()) for _ in range(n)]
for _ in range(q):
    temp = 0
    t = int(input())
    for i in range(n):
        temp += musiclist[i]
        if temp > t:
            print(i + 1)
            break