while True:
    word = input()
    if word == '#':
        break
    for i in range(len(word)):
        if word[i] in 'aeiou':
            print(word[i:] + word[:i] + 'ay')
            break
    else:
        print(word + 'ay')
