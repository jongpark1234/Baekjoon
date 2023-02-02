s = input()
for i in range(2, len(s), 2):
    for j in range(len(s) - i):
        temp = s[j:j + i]
        if temp == temp[::-1]:
            print('Or not.')
            exit()
print('Odd.')
