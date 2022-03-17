s = input()
substrings = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        substrings.add(s[i:j + 1])
print(len(substrings))
