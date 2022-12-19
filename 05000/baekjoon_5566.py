current = 1
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
for i in range(m):
    current += int(input())
    if current > n:
        print(i + 1)
        break
    current += arr[current - 1]
    if current >= n:
        print(i + 1)
        break
