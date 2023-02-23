n, m = map(int, input().split())
for _ in range(int(input())):
    e = int(input())
    print(e, e * n if e <= 1000 else n * 1000 + (e - 1000) * m)
