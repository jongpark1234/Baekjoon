while (n := int(input())) != 0:
    grundy = 0
    k = list(map(int, input().split()))
    for i in k:
        grundy ^= i
    print(sum([grundy ^ i < i for i in k]))
