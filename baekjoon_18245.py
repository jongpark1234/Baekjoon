line = 1
while True:
    line += 1
    s = input()
    if s == 'Was it a cat I saw?':
        break
    for i in range(0, len(s), line):
        print(s[i], end='')
    print()
