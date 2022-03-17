s = input()
wordlist = ['U', 'C', 'P', 'C']
ucpc = True
for i in range(4):
    if wordlist[i] in s:
        index = s.find(wordlist[i])
        s = s[index + 1:]
    else:
        ucpc = False
        break
print('I love UCPC' if ucpc else 'I hate UCPC')
