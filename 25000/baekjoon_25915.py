result = 0
c = input()
for i in 'ILOVEYONSEI':
    result += abs(ord(i) - ord(c))
    c = i
print(result)
