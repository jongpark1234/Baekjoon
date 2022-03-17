s = input()
num = 0
isprime = True
for i in s:
    if i.isupper():
        num += ord(i) - 38
    else:
        num += ord(i) - 96
for i in range(2, int(num ** (1 / 2)) + 1):
    if num % i == 0:
        isprime = False
if isprime:
    print('It is a prime word.')
else:
    print('It is not a prime word.')
