def dp(result, n, m, i, j, s1, s2): # 진행우선방향 : 아래->오른쪽
    value1, value2 = 0, 0
    if j == m:
        if s1 == 1 << n: 
            return True
        else:
            return False
    if i == n + 1:
        return False
    if i == n:
        s1 = s2
        s2 = 1 << n
        return dp(result, n, m, 0, j + 1, s1, s2)
    else:
        if s2 == (1 << n) and result[i][j][s1] != -1:
            return result[i][j][s1]
        if s1 & 1 << i:
            value1 = dp(result, n, m, i + 1, j, s1, s2) 
        else:
            value1 = dp(result, n, m, i + 1, j, s1, s2 + (1 << i))
            if not (s1 & 1 << (i + 1)):
                value2 = dp(result, n, m, i + 2, j, s1, s2)
    total = (value1 + value2) % 9901
    if s2 == (1 << n):
        result[i][j][s1] = total
    return total
n, m = map(int, input().split())
result = [[[-1] * (1 << (n + 1)) for _ in range(m)] for _ in range(n)]
s1 = 1 << n
s2 = 1 << n
print(dp(result, n, m, 0, 0, s1, s2))
