from itertools import permutations
def transform(n, d):
    result = ''
    while n > 0:
        n, mod = divmod(n, d)
        result += str(mod)
    return result[::-1] 
n, d = map(int, input().split())
n = int(transform(n, d))
numlist = [i for i in range(d)]
numlist = list(permutations(numlist))
if n >= int(''.join(map(str, list(numlist[-1])))):
    print(-1)
else:
    for i in numlist:
        num = ''.join(map(str, list(i)))
        if num[0] == '0':
            continue
        if int(num) > n:
            print(int(num, d))
            break
