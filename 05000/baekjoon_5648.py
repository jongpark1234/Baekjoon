n, *numlist = input().split()
while len(numlist) != int(n):
    numlist += input().split()
print(*sorted(map(lambda x: int(x[::-1]), numlist)))
