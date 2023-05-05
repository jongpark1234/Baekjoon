def convert(n, q):
    ret = ''
    while n:
        n, mod = divmod(n, q)
        ret += str(mod) if mod < 10 else chr(mod + 55)
    return ret[::-1]
n, b = map(int, input().split())
print(convert(n, b))
