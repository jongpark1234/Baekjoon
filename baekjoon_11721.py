s = input()
times = 0
for i in range(len(s)):
    if times == 10:
        print('')
        times = 0
    print(s[i], end='')
    times += 1
