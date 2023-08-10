n, m = map(int, input().split())
if n:
    cur, result = 0, 1
    for i in map(int, input().split()):
        if cur + i > m:
            result += 1
            cur = 0
        cur += i
    print(result)
else:
    print(0)
