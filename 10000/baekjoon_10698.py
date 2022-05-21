for i in range(int(input())):
    Input = input().split()
    result = 'NO'
    if Input[1] == '+' and int(Input[0]) + int(Input[2]) == int(Input[4]):
        result = 'YES'
    if Input[1] == '-' and int(Input[0]) - int(Input[2]) == int(Input[4]):
        result = 'YES'
    print(f'Case {i + 1}: {result}')
