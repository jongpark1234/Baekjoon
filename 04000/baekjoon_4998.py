for tc in [*open(0)]:
    result = 0
    n, b, m = map(float, tc.split())
    while n <= m:
        result += 1
        n *= 1 + b / 100
    print(result)
