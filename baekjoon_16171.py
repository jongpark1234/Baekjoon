s = input()
k = input()
new_s = ''
for i in s:
    if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        new_s += i
print(int(k in new_s))
