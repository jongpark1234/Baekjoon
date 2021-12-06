a = int(input(), 2)
b = int(input(), 2)
print(f'{int(bin(a & b)[2:]):010d}')
print(f'{int(bin(a | b)[2:]):010d}')
print(f'{int(bin(a ^ b)[2:]):010d}')
for i in bin(a)[2:].zfill(10):
    if i == '0':
        print('1', end='')
    else:
        print('0', end='')
print()
for i in bin(b)[2:].zfill(10):
    if i == '0':
        print('1', end='')
    else:
        print('0', end='')
