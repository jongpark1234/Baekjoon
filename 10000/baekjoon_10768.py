month = int(input())
day = int(input())
if month > 2:
    print('After')
elif month < 2:
    print('Before')
else:
    if day > 18:
        print('After')
    elif day < 18:
        print('Before')
    else:
        print('Special')
