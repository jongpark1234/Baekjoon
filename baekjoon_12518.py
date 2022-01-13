vowel = 'aeiouAEIOU'
for i in range(int(input())):
    name = input()
    if name[-1] in 'yY':
        ruled = 'nobody'
    elif name[-1] in vowel:
        ruled = 'a queen'
    else:
        ruled = 'a king'
    print(f'Case #{i + 1}: {name} is ruled by {ruled}.')
