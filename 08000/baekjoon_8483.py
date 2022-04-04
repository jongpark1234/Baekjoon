def F(a, b, c):
    if a < b:
        a, b = b, a
    if c // a < 101:
        ret = 0
        for i in range(1, c // a + 1):
            ret += (c - a * i) // b
        return ret
    return (((((a // b) * c + (a % b)) // a) - 1) // (a // b) * (2 * (((a // b) * c + (a % b)) // a) - (a // b) * (1 + ((((a // b) * c + (a % b)) // a) - 1) // (a // b))) // 2) + F(b, a % b, c - b * (((a // b) * c + (a % b)) // a))
a, b, c = map(int, input().split())
print(F(a, b, c) + c // a + c // b + 1)
