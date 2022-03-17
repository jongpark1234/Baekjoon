from re import split
num = []
for _ in range(int(input())):
    s = input()
    num += split(r'[a-z]', s)
print('\n'.join(list(map(str, sorted(list(map(int, list(filter(lambda x: x != '', num)))))))))
