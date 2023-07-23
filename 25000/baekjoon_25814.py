a, b = map(lambda x: len(x) * sum(int(i) for i in x), input().split())
print(1 if a > b else 2 if a < b else 0)
