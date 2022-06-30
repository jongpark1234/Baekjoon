def calc(x, y):
    return x[0] * y[0] + x[1] * y[1]
def solve(a, b, v, r):
    d = [b[i] - a[i] for i in range(2)]
    a, b, c = calc(v, v), calc(v, d) * -2, calc(d, d) - (r * 2) ** 2
    if a < 0:
        return -1
    value = b ** 2 - 4 * a * c
    if value < 0:
        return -1
    return -1 if (temp := (-b - value ** 0.5) / (a * 2)) < 0 else temp
result = 0
v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
*v4, r = list(map(int, input().split()))
t1, t2 = solve(v1, v2, v4, r), solve(v1, v3, v4, r)
if (t1 == -1 or t2 < t1) and t2 != -1:
    result += 1
    v2, v3 = v3[:], v2[:]
    t1, t2 = t2, t1
print(5 if t1 == -1 else result + 3 if solve(v2, v3, [v2[i] - (v1[i] + v4[i] * t1) for i in range(2)], r) == -1 else result + 1)
