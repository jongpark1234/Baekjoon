for i in input():
    if i.isalpha():
        temp = ord(i) + 13
        if i.isupper() and temp > 90:
            temp -= 26
        elif i.islower() and temp > 122:
            temp -= 26
        print(chr(temp), end='')
    else:
        print(i, end='')
