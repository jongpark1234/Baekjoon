s = input()
print('Correct' if s[:2] == 'io' and s[2:].isdecimal() else 'Incorrect')
