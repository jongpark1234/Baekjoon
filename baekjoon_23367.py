keys = ['qwertasdfgzxcvb', 'yuiophjklnm']
s = input()
direction = 0 if s[0] in keys[1] else 1
for i in s[1:]:
    if i not in keys[direction]:
        print('no')
        exit(0)
    direction = not direction
else:
    print('yes')
