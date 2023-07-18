for _ in range(int(input())):
    digit = input()
    ab, cd = int(digit[:2]), int(digit[2:])
    print('YES' if (ab ** 2 + cd ** 2) % 7 == 1 else 'NO')
