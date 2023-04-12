arr = [input() for _ in range(36)]
if len(set(arr)) == 36:
    for i in range(35):
        if abs((ord(arr[i][0]) - ord(arr[i + 1][0])) * (int(arr[i][1]) - int(arr[i + 1][1]))) != 2:
            print('Invalid')
            break
    else:
        for i, j in [[-2, -1], [-2, 1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2]]:
            r = ord(arr[-1][0]) + i
            c = int(arr[-1][1]) + j
            if 65 <= r <= 90 and 1 <= c <= 6:
                if chr(r) == arr[0][0] and c == int(arr[0][1]):
                    print('Valid')
                    break
        else:
            print('Invalid')
else:
    print('Invalid')
