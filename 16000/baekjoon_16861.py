n = int(input())
while n % sum(map(int, str(n))):
    n += 1
print(n)
