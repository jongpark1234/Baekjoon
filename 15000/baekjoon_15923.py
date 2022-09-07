result = 0
n = int(input())
a, b = map(int, input().split())
A, B = a, b
for _ in range(n - 1):
    r, c = map(int, input().split())
    result += abs(a - r) + abs(b - c)
    a, b = r, c
print(result + abs(A - a) + abs(B - b))
