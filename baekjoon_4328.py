while True:
    try:
        b, p, m = map(int, input().split())
        n = int(str(p), b) % int(str(m), b)
        result = ''
        while n >= b:
            n, mod = divmod(n, b)
            result += str(mod)
        result += str(n)
        print(result[::-1])
    except:
        break
