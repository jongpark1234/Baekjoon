def solve(n):
    ret = 1
    for i in n:
        ret *= int(i)
    return str(ret)
result = 0
n = input()
while len(n) > 1:
    result += 1
    n = solve(n)
print(result)
