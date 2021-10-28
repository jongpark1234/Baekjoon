x = input()
if x[0] == '0':
    if x[1] == 'x':
        print(int(x, 16))
    else:
        print(int(x, 8))
else:
    print(x)
