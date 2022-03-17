for i in range(int(input())):
    country = input()
    if country[-1] in 'aeiouAEIOU':
        rule = 'a queen'
    elif country[-1] in 'yY':
        rule = 'nobody'
    else:
        rule = 'a king'
    print(f'Case #{i + 1}: {country} is ruled by {rule}.')
