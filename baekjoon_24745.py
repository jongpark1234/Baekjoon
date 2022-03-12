Morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
converted = ''
for i in input().upper():
    if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890':
        continue
    if i.isdecimal():
        converted += Morse[ord(i) - 22]
    else:
        converted += Morse[ord(i) - 65]
print(['NO', 'YES'][bool(converted == converted[::-1] and len(converted))])
