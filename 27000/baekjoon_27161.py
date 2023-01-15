time = 0
acc = 1
n = int(input())
for _ in range(n):
    s, x = input().split()
    time += acc
    if time == 0:
        time = 12
    elif time == 13:
        time = 1
    if time != int(x) and s == 'HOURGLASS':
        acc *= -1
    print(time, 'YES' if time == int(x) and s != 'HOURGLASS' else 'NO')
