previous = ''
while True:
    n = input()
    if n == '99999':
        break
    code = sum(map(int, n[:2]))
    previous = previous if code == 0 else 'left' if code & 1 else 'right'
    print(previous, int(n[2:]))
