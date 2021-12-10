p1, q1, p2, q2 = map(int, input().split())
S = p1 * p2 / q1 / q2 / 2
print(1 if int(S) == S else 0)
