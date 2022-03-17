for _ in range(int(input())):
    value = 0
    plate = input().split('-')
    seq = len(plate[0])
    for i in range(3):
        value += (ord(plate[0][i]) - 65) * 26 ** (2 - i)
    if abs(value - int(plate[1])) > 100:
        print('not', end=' ')
    print('nice')
