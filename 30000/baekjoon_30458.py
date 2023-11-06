n = int(input())
s = list(input())
alDict = { chr(97 + i): 0 for i in range(26) }
for i in s[:n // 2] + s[-(n // 2):]:
    alDict[i] += 1
print('Yes' if all(map(lambda x: x % 2 == 0, alDict.values())) else 'No')
