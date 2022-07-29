n = int(input())
print(32 if n < 0 else 1 if n == 0 else len(bin(n)[2:]))
