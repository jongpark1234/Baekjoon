temp = 3
for _ in range(10):
    match int(input()):
        case 1:
            temp += 1
        case 2:
            temp += 2
        case 3:
            temp -= 1
    temp &= 3
print({ 0: 'E', 1: 'S', 2: 'W', 3: 'N' }[temp])
