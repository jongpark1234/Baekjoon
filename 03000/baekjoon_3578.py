n = int(input())
print(n ^ 1 if n < 2 else ('4' if n & 1 else '') + '8' * (n - (n & 1) >> 1))
