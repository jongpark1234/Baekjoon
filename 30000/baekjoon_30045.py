result = 0
for _ in range(int(input())):
    s = input()
    result += '01' in s or 'OI' in s
print(result)
