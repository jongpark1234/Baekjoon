now = list(map(int, input().split(':')))
throw = list(map(int, input().split(':')))
now = now[0] * 3600 + now[1] * 60 + now[2]
throw = throw[0] * 3600 + throw[1] * 60 + throw[2]
if now > throw:
    throw += 86400
time = throw - now
if now == throw:
    print('24:00:00')
else:
    print(f'{time // 3600:02d}:{time % 3600 // 60:02d}:{time % 60:02d}')
