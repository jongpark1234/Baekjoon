while True:
    try:
        chicken = 0
        stamp = 0
        n, k = map(int, input().split())
        while n:
            chicken += n
            stamp += n
            n = stamp // k
            stamp = stamp % k
        print(chicken)
    except EOFError:
        break
