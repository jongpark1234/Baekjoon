record = input()
a = b = 0
for i in range(0, len(record), 2):
    if record[i] == 'A':
        a += int(record[i + 1])
    else:
        b += int(record[i + 1])
    if max(a, b) > 10:
        if max(a, b) - min(a, b) > 1:
            print('A' if a > b else 'B')
            break
