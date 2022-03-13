def smaller(x, y):
    return x if x < y else y
amount = 0
i = 0
w = False
n, b, c = map(int, input().split())
A = list(map(int, input().split()))
if c < b:
    while i < n:
        if i < n - 2 and A[i] and A[i + 1] and A[i + 2]:
            if w:
                s = smaller(A[i], A[i + 1])
                A[i] -= s
                A[i + 1] -= s
                amount += (b + c) * s
                w = False
            else:
                s = smaller(smaller(A[i], A[i + 1]), A[i + 2])
                if A[i] < A[i + 1] and A[i + 1] > A[i + 2]:
                    s -= smaller(smaller(A[i], A[i + 2]), smaller(A[i + 1] - A[i], A[i + 1] - A[i + 2]))
                    w = True
                A[i] -= s
                A[i + 1] -= s
                A[i + 2] -= s
                amount += (b + c * 2) * s
                continue
        if i < n - 1 and A[i] and A[i + 1]:
            s = smaller(A[i], A[i + 1])
            A[i] -= s
            A[i + 1] -= s
            amount += (b + c) * s
        if A[i]:
            s = A[i]
            A[i] = 0
            amount += s * b
        i += 1
else:
    for i in range(n):
        amount += A[i] * b
print(amount)