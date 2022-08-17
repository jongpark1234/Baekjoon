operators = ['== +', '== -', '== *', '== /', '+ ==', '- ==', '* ==', '/ ==']
a, b, c = map(int, input().split())
for i in operators:
    j = i.split()
    f = f'{a}{j[0]}{b}{j[1]}{c}'
    if eval(f):
        f = f.replace('==', '=')
        print(f)
