n, *chars = map(int, open(0).read().split())
print(sorted(chars, reverse=True).index(chars[0]) + 1)
