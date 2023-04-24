w, n, p = map(int, input().split())
print(sum(map(lambda x: n >= int(x) >= w, input().split())))
