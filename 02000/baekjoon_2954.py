idx = 0
result = ''
diary = input()
while idx < len(diary):
    result += diary[idx]
    if diary[idx] in 'aeiou':
        idx += 3
    else:
        idx += 1
print(result)
