a, b = map(int, input().split())
print(+(a - (a * b / 100) < 100))