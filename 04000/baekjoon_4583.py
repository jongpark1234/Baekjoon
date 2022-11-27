while True:
    s, result = input(), ''
    if s == '#':
        break
    for i in s[::-1]:
        if i not in 'bdpqiovwx':
            print('INVALID')
            break
        result += 'b' if i == 'd' else 'd' if i == 'b' else 'p' if i == 'q' else 'q' if i == 'p' else i
    else:
        print(result)
