n, c = map(int, input().split())
time = -c * (n - 1)
for _ in range(n):
    m, s = map(int, input().split(':'))
    time += m * 60 + s
print(f'{time // 3600:02d}:{time % 3600 // 60:02d}:{time % 60:02d}')
