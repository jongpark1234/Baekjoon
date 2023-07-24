result = coffee = 0
n = int(input())
s = input()
for i in s:
    if i == '1':
        result += 1
        coffee = 2
    else:
        result += coffee > 0
        coffee = max(coffee - 1, 0)
print(result)
