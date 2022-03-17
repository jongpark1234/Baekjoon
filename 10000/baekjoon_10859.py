# pypy3
def isprime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if not num % i:
            return False
    return True
wrong = False
num = input()
revnum = ''
for i in num[::-1]:
    if i in '347':
        wrong = True
        break
    elif i in '01258':
        revnum += i
    elif i == '6':
        revnum += '9'
    elif i == '9':
        revnum += '6'
print('yes' if not wrong and isprime(int(num)) and isprime(int(revnum)) else 'no')
