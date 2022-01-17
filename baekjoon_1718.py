plain = input()
key = input() * 30000
cipher = ''
for i in range(len(plain)):
    if plain[i] == ' ':
        cipher += ' '
    else:
        temp = ord(plain[i]) - (ord(key[i]) - 96)
        if temp < 97:
            cipher += chr(temp + 26)
        else:
            cipher += chr(temp)
print(cipher)
