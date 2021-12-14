words = []
while True:
    line = input()
    new_line = ''
    for i in line:
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz- ':
            new_line += i
    words += new_line.split()
    if 'E-N-D' in words:
        break
length = 0
for i in words:
    if len(i) > length:
        word = i
        length = len(i)
print(word.lower())
