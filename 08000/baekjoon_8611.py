def solution(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]
n = int(input())
palindrome = False
for i in range(2, 11):
    num = solution(n, i)
    if num == num[::-1]:
        palindrome = True
        print(i, num)
if not palindrome:
    print('NIE')
