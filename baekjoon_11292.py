while True:
    n = int(input())
    if n == 0:
        break
    tall = [input().split() for _ in range(n)]
    Max = sorted(tall, key = lambda x: -float(x[1]))[0][1]
    for i in tall:
        if i[1] == Max:
            print(i[0], end=' ')
