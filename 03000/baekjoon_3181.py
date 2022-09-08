wordlist = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
s = input()
result = s[0][0]
for i in s.split()[1:]:
    if i not in wordlist:
        result += i[0]
print(result.upper())
