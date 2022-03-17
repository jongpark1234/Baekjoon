s = ''
for i in input():
    if len(s) == 0 or not s[-1] == i:
        s += i
print(s)
