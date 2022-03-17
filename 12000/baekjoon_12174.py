for i in range(int(input())):
    b = int(input())
    s = input().replace('I', '1').replace('O', '0')
    translated = ''
    for j in range(0, len(s), 8):
        translated += chr(int(s[j:j + 8], 2))
    print(f'Case #{i + 1}: {translated}')
