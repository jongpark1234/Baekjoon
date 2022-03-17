for i in range(int(input())):
    h = int(input())
    for j in input():
        if j == 'c':
            h += 1
        else:
            h -= 1
    print(f'Data Set {i + 1}:\n{h}')
    print()
