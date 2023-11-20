result = 0
s = input()
for i in range(len(s)):
    if s[i] == 'KOREA'[result % 5]:
        result += 1
print(result)
