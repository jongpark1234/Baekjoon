from sys import stdin
right = set()
wrong = {}
count = 0
for i in range(int(input())):
    number, name, result, memory, time, language, length = stdin.readline().rstrip().split()
    if name == 'megalusion':
        continue
    if result == '4':
        right.add(name)
    else:
        if name not in right:
            try:
                wrong[name] += 1
            except:
                wrong[name] = 1
for i in wrong.keys():
    if i in right:
        count += wrong[i]
print(len(right) / (len(right) + count) * 100 if len(right) else 0)
