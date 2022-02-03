codes = []
while True:
    try:
        codes.append(input())
    except EOFError:
        break
for i in codes:
    while 'BUG' in i:
        i = i.replace('BUG', '')
    print(i)
