data = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    try:
        result = ''
        n, s = input().split()
        for i in s:
            result += data[(data.index(i) + int(n)) % len(data)]
        print(result[::-1])
    except ValueError:
        break
