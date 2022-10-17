vowel = 'aeiou'
s = input()
for i in range(len(s) - 1):
    if not (s[i] in vowel) ^ (s[i + 1] in vowel):
        print(0)
        break
else:
    print(1)
