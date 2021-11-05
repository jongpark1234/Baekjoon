wordlist1 = [0 for i in range(26)]; wordlist2 = [0 for i in range(26)]
result = 0
s1 = input()
s2 = input()
for i in s1:
    wordlist1[ord(i) - 97] += 1
for i in s2:
    wordlist2[ord(i) - 97] += 1
for i in range(26):
    if wordlist1[i] != wordlist2[i]:
        result += abs(wordlist1[i] - wordlist2[i])
print(result)
