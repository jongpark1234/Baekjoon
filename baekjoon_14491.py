n = int(input())
rev_base = ''
while n > 0:
    n, mod = divmod(n, 9)
    rev_base += str(mod)
print(rev_base[::-1])
