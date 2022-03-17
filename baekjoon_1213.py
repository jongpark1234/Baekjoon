s = input()
word = [0] * 26
for i in s:
    word[ord(i) - 65] += 1
odd = 0
middle = ''
string = ''
for i in range(26):
    if word[i] % 2:
        odd += 1
        middle = chr(i + 65)
    string += chr(i + 65) * (word[i] // 2)
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(string + middle + string[::-1])
