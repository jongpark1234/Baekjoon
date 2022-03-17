n, w, h, l = map(int, input().split())
print((w // l) * (h // l) if (w // l) * (h // l) <= n else n)
