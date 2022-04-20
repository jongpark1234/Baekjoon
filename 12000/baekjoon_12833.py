a, b, c = map(int, input().split())
print(a ^ b if c & 1 else a)
