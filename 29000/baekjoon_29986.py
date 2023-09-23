n, h = map(int, input().split())
print(sum(map(lambda x: int(x) <= h, input().split())))
