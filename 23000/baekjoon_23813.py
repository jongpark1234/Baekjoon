n = input()
result = 0
for i in range(len(n)):
    result += int(n[i:] + n[:i])
print(result)
