a, b = map(int, input().split())
print(min(a % 2 * b, b % 2 * a))
