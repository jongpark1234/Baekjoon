x, n = map(int, input().split())
if n & 1 and n != 1:
    print('ERROR')
elif (x < 0 and n == 1) or (x > 0 and n == 0):
    print('INFINITE')
elif n != 0 and x > 0 and not n & 1:
    temp = n >> 1
    print((x + temp - 1) // temp - 1)
else:
    print(0)
