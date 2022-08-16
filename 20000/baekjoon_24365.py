a, b, c = map(int, input().split())
avg = (a + b + c) // 3
print((avg - a) * 2 + avg - b)
