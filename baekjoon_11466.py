h, w = map(int, input().split())
a, b = max(h, w), min(h, w)
s1 = a / 3 if a / 3 <= b else b
s2 = b / 2
print(max(s1, s2))
