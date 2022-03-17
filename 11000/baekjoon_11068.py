def base(n, q):
    result = ''
    while n > 0:
        n, mod = divmod(n, q)
        if mod > 9:
            mod = chr(mod + 55)
        result += str(mod)
    return result
for _ in range(int(input())):
    palindrome = False
    s = int(input())
    for i in range(2, 65):
        num = base(s, i)
        if num == num[::-1]:
            palindrome = True
            break
    print(1 if palindrome else 0)
