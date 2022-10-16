g, p, t = map(int, input().split())
a, b = g * p, g + t * p
print(1 if a < b else 2 if a > b else 0)
