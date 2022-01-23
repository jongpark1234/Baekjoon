for i in range(int(input())):
    a, b = input().split()
    print(f'Case {i + 1}:', end=' ')
    if a == b:
        print('Login successful.')
        continue
    else:
        if a == b.swapcase():
            print('Wrong password. Please, check your caps lock key.')
            continue
        else:
            temp = ''
            for j in a:
                if j.isalpha():
                    temp += j
            if temp == b:
                print('Wrong password. Please, check your num lock key.')
                continue
            elif temp == b.swapcase():
                print('Wrong password. Please, check your caps lock and num lock keys.')
                continue
    print('Wrong password.')
