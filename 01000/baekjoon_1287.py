s = input()
if s.count('()'):
    print('ROCK')
else:
    try:
        eval(''.join(['|' if i in '+-*/' else i for i in s]))
        print(eval(s.replace('/', '//')))
    except:
        print('ROCK')
