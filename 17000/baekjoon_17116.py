block = input()
obstacle = input()
if block == 'KEY IS PUSH AND OPEN DOOR IS SHUT' and obstacle == 'KEY DOOR':
    print('BABA IS WIN')
elif block == 'BABA IS ROCK' and obstacle == 'ROCK':
    print('BABA IS NOT WIN')
elif block == 'LONELY FLAG IS BABA' and obstacle == 'ROCK':
    print('BABA IS WIN')
else:
    print('BABA IS NOT WIN')
