temp = 0
s = input()
l = len(s)
while temp < l:
    print(s[temp], end='')
    temp += ord(s[temp]) - 64
