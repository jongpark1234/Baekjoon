while True:
    num = list(map(int, input()))
    if num == ['0']:
        break
    result = []
    for i in num:
        if i == '0':
            result.append(4)
        elif i == '1':
            result.append(2)
        else:
            result.append(3)
    print(sum(result) + len(result) + 1)
