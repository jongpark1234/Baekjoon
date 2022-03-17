for _ in range(int(input())):
    s = list(map(int, input().split()))
    hp = max(s[0] + s[4], 1)
    mp = max(s[1] + s[5], 1) * 5
    at = (max(s[2] + s[6], 0)) * 2
    df = (s[3] + s[7]) * 2
    print(hp + mp + at + df)
