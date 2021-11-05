while True:
    wordlist = [0 for i in range(26)]
    s = input()
    if s == '*':
        break
    for i in s:
        if not i == ' ':
            wordlist[ord(i) - 97] += 1
    print('Y' if not wordlist.count(0) else 'N')
