tc = 0
while True:
    tc += 1
    query = input()
    if query.split()[1] == 'E':
        break
    print(f'Case {tc}: {str(eval(query)).lower()}')
