for i in range(int(input())):
    string = ''
    for j in input():
        if j == 'Z':
            j= 65
        else:
            j = ord(j) + 1
        string += chr(j)
    print(f'String #{i + 1}')
    print(string)
    print()
