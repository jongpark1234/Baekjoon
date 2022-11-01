while True:
    s = input()
    if s == 'I quacked the code!':
        break
    print('*Nod*' if s[-1] == '.' else 'Quack!')
