import sys
wordlist, s = [0 for x in range(26)], sys.stdin.read()
for i in s:
    if i.islower():
        wordlist[ord(i) - 97] += 1
for i in range(26):
    if wordlist[i] == max(wordlist):
        print(chr(i + 97), end='')
