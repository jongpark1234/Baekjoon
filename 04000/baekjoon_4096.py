from sys import stdin
while True:
    palindrometer = 0
    num = stdin.readline().rstrip()
    if num == '0':
        break
    length = len(num)
    while num != num[::-1]:
        num = str(int(num) + 1).zfill(length)
        palindrometer += 1
    print(palindrometer)
