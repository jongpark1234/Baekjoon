while True:
    name, age, weight = input().split()
    if f'{name}{age}{weight}' == '#00':
        break
    print(name, 'Senior' if int(age) > 17 or int(weight) > 79 else 'Junior')
