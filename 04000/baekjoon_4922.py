while True:
    result, cnt = 0, 1
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        result += cnt
        cnt += 2
    print(f'{n} => {result - n + 1}')
