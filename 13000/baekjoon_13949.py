k, n = map(int, input().split())
used = set([0])
result = set()
result.add((0, 1, k))
while n:
    temp = result.copy()
    for a, b, c in result:
        if a not in used and b not in used and c not in used and a != b and b != c:
            used.add(a)
            used.add(b)
            used.add(c)
            print(a, b, c)
            n -= 1
            if n == 0:
                break
        for _ in range(3):
            d = k * (a + b) - c
            if d > -1:
                temp.add(tuple(sorted([a, b, d])))
            a, b, c = b, c, a
    result = temp
