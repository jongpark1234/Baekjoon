while True:
    try:
        numlist = [0, 0, 0, 0]
        for i in input():
            if 97 <= ord(i) <= 122:
                numlist[0] += 1
            elif 65 <= ord(i) <= 90:
                numlist[1] += 1
            elif 48 <= ord(i) <= 57:
                numlist[2] += 1
            elif ord(i) == 32:
                numlist[3] += 1
        print(' '.join(map(str, numlist)))
    except EOFError:
        break
