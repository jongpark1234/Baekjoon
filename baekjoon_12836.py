n, q = map(int, input().split())
day = [0] * n
for _ in range(q):
    a, p, x = map(int, input().split())
    if a == 1:
        day[p - 1] += x
    else:
        print(sum(day[p - 1:x]))
