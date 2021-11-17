message = input()
sad = message.count(':-(')
happy = message.count(':-)')
if sad == happy == 0:
    print('none')
elif sad == happy:
    print('unsure')
elif sad > happy:
    print('sad')
else:
    print('happy')
