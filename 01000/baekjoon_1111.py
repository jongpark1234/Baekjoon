n = int(input())
m = list(map(int, input().split()))
if n == 1:
    print('A')
elif n == 2:
    if m[0] == m[1]:
        print(m[0])
    else:
        print('A')
else:
    a = 0
    x, y = m[1] - m[0], m[2] - m[1]
    if x != 0:
        a = y // x
    b = m[1] - a * m[0]
    for i in range(1, n):
        if m[i] != (m[i - 1] * a + b):
            break
    else:
        print(m[n - 1] * a + b)
        exit(0)
    print('B')
