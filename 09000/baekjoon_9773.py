for _ in range(int(input())):
    n = input()
    IDKey = sum(map(int, n)) + int(n[-3:] + '0')
    print(str(IDKey + (1000 if IDKey < 1000 else 0))[-4:])
