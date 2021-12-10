time = sorted(list(map(int, input().split())))
if time[0] == time[1] or time[1] == time[2] or time[0] == time[2] or time[0] + time[1] == time[2]:
    print('S')
else:
    print('N')
