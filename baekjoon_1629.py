from sys import stdin
def powdef(x, y):
    if y == 1:
        return x % c
    else:
        result = powdef(x, int(y / 2))
        if y % 2 == 0:
            return result * result % c
        else:
            return result * result * x % c
a, b, c = map(int, stdin.readline().split())
print(powdef(a, b))