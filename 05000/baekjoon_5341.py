while True:
    n = int(input())
    if n == 0:
        break
    print(sum(i for i in range(1, n + 1)))
