from math import factorial
def backtrack(x, idx):
    global temp
    if idx == len(s):
        temp += 1
        if temp == n:
            return x
    else:
        for i in s:
            if i not in x:
                ret = backtrack(x + i, idx + 1)
                if ret:
                    return ret
    return None
while True:
    try:
        temp = 0
        s, n = input().split()
        n = int(n)
        if factorial(len(s)) < n:
            print(f'{s} {n} = No permutation')
        else:
            print(f'{s} {n} =', backtrack('', 0))
    except EOFError:
        break
