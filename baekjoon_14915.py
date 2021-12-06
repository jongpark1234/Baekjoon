def change(n, q):
    if n == 0:
        return 0
    temp = ''
    while n > 0:
        n, mod = divmod(n, q)
        if mod >= 10:
            temp += chr(mod + 55)
        else:
            temp += str(mod)
    return temp[::-1]
print(change(*map(int, input().split())))
