for _ in range(int(input())):
    s, i, j = map(lambda x: int(x) if x.isnumeric() else x, input().split())
    print(s[:i] + s[j:])
