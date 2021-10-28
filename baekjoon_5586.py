s = input()
keyword = [0, 0]
for i in range(len(s) - 2):
    string = s[i] + s[i + 1] + s[i + 2]
    if string == 'JOI':
        keyword[0] += 1
    if string == 'IOI':
        keyword[1] += 1
print(keyword[0], keyword[1], sep='\n')
