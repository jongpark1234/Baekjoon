a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
print(0 if a1 * n0 + a0 > c * n0 else 1 if a1 <= c else 0)
