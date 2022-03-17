idx = 0
while True:
    idx += 1
    n = int(input())
    if n == 0:
        break
    result = int(input())
    for i in range(n - 1):
        if i == n - 2:
            result += sum(map(int, input().split()))
        else:
            a = list(map(int, input().split()))
            result += a[0] + a[-1]
    print(f'Case #{idx}:{result}')
