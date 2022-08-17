while True:
    result = 1
    a, *branch = list(map(int, input().split()))
    if a == 0:
        break
    for i in range(a):
        result = result * branch[i << 1] - branch[(i << 1) + 1]
    print(result)
