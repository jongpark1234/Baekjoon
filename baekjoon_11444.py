from sys import stdin
def power(matrix, n):
    if n == 1:
        return matrix
    elif n % 2:
        return multi(power(matrix, n - 1), matrix)
    else:
        return power(multi(matrix, matrix), n // 2)
def multi(a,b):
    temp=[[0] * len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum = 0
            for k in range(2):
                sum += a[i][k] * b[k][j]
            temp[i][j] = sum % 1000000007
    return temp
matrix = [[1, 1], [1, 0]]
start = [[1], [1]]
n = int(stdin.readline())
if n < 3:
    print(1)
else:
    print(multi(power(matrix, n - 2), start)[0][0])
