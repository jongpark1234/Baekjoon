while (n := int(input())):
    a = list(map(lambda x: abs(int(x) - 2023), input().split()))
    print(a.index(min(a)) + 1)
