repeat = 0
for _ in range(int(input())):
    code = input()
    repeat = max(repeat, code.count('for') + code.count('while'))
print(repeat)
