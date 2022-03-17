while True:
    a = input()
    if a == 'ENDOFINPUT':
        break
    if a == 'START' or a == 'END':
        continue
    else:
        for i in a:
            print(i if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' else chr(ord(i) - 5) if ord(i) > ord('E') else chr(ord(i) + 21), end='')
        print()
