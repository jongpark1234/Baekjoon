s, *c = map(int, input().split())
print(sum(map(lambda x: s - x <= 1000, c)))
