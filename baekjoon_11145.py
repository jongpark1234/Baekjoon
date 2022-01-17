for i in range(int(input())):
    number = input().strip()
    if not ' ' in number and number.isdecimal():
        print(int(number))
    else:
        print('invalid input')
