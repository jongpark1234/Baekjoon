result = 0
n = int(input())
while n:
    result += 1
    n = int(str(n).replace('1', '', 1)) if n != 1 and '1' in str(n) else n - 1
print(result)
