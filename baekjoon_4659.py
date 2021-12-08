from sys import stdin
vowel = 'aeiou'
consonant = 'bcdfghjklmnpqrstvwxyz'
while True:
    isvowel = False
    v, c = 0, 0
    word = ''
    s = stdin.readline().rstrip()
    Not = ''
    if s == 'end':
        break
    for i in s:
        if i in 'aeiou':
            isvowel = True
            break
    for i in s:
        if i in vowel:
            c = 0
            v += 1
        else:
            v = 0
            c += 1
        word += i
        if not isvowel:
            Not = 'not '
            print('not vowel')
            break
        if len(word) > 1:
            if word[-2] == word[-1] and (word[-1] != 'e' and word[-1] != 'o'):
                Not = 'not '
                break
        if len(word) > 2:
            if word[-3] == word[-2] == word[-1] and (word[-1] == 'e' and word[-1] == 'o'):
                Not = 'not '
                break
        if v == 3 or c == 3:
            Not = 'not '
            break
    print(f'<{s}> is {Not}acceptable.')
