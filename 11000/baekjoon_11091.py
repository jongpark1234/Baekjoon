for _ in range(int(input())):
    alphabet = [0 for i in range(26)]
    s = input().upper()
    for i in s:
        if 64 < ord(i) < 91:
            alphabet[ord(i) - 65] = 1
    if 0 not in alphabet:
        print('pangram')
    else:
        miss = ''
        for i in range(26):
            if alphabet[i] == 0:
                miss += chr(i + 65)
        print('missing', miss.lower())
