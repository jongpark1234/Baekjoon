from sys import stdin
MOD = 998244353
def check1(idx: int) -> bool:
    for i in range(1, n * 2 + 2):
        if s[idx][i] == '?':
            continue
        if (i & 1 and s[idx][i] != a) or (~i & 1 and s[idx][i] != b):
            return False
    return True
def check2(idx: int) -> bool:
    for i in range(1, n * 2 + 2, 2):
        if s[idx][i] != c and s[idx][i] != '?':
            return False
    for i in range(2, n * 2 + 2, 2):
        if s[idx][i] == c:
            return False
    return True
def check3() -> bool:
    for i in range(2, n * 2 + 2, 2):
        if s[0][i] != c and s[0][i] != '?':
            return False
        if s[1][i] != c and s[1][i] != '?':
            return False
    return True
def solve1(idx: int) -> int:
    flag, ret = True, 0
    for i in range(2, n * 2 + 2, 2):
        if s[idx][i] == a:
            flag = 0
        elif s[idx][i] == '?':
            ret += 1
    return (pow(2, ret, MOD) - flag) % MOD
def solve2() -> int:
    temp, ret = n * 2 + 2, 0
    for i in range(n * 2 + 1, 0, -2):
        if s[0][i] == b or s[0][i] == c or s[1][i] == a or s[1][i] == c:
            break
        temp = i
    for i in range(1, n * 2 + 2, 2):
        if s[0][i] == a or s[0][i] == c or s[1][i] == b or s[1][i] == c:
            break
        if i + 2 >= temp:
            ret += 1
    return ret
for _ in range(int(stdin.readline())):
    result = 0
    n = int(stdin.readline())
    s = [' ' + stdin.readline() for _ in range(2)]
    for i in range(1, 4):
        for j in range(1, 4):
            if not (i ^ j):
                continue
            a, b, c = chr(i + 64), chr(j + 64), chr((i ^ j) + 64)
            for k in range(2):
                if check1(k) and check2(k ^ 1):
                    result = (result + solve1(k ^ 1)) % MOD
            if check3():
                result = (result + solve2()) % MOD
    print((result + MOD) % MOD)
