for _ in range(int(input())):
    d, s, m, t = map(int, input().split())
    print(d, s + m + t, 'PASS' if s > 10 and m > 7 and t > 11 and s + m + t > 54 else 'FAIL')
