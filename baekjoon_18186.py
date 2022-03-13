amount = 0
i = 0
w = False
n, b, c = map(int, input().split())
A = list(map(int, input().split()))
if c < b:
    while i < n:
        if i < n - 2 and A[i] and A[i + 1] and A[i + 2]:
            if w:
                s = min(A[i], A[i + 1])
                A[i] -= s
                A[i + 1] -= s
                amount += (b + c) * s
                w = False
            else:
                s = min(min(A[i], A[i + 1]), A[i + 2])
                if A[i] < A[i + 1] and A[i + 1] > A[i + 2]:
                    s -= min(min(A[i], A[i + 2]), min(A[i + 1] - A[i], A[i + 1] - A[i + 2]))
                    w = True
                A[i] -= s
                A[i + 1] -= s
                A[i + 2] -= s
                amount += (b + c * 2) * s
                continue
        if i < n - 1 and A[i] and A[i + 1]:
            s = min(A[i], A[i + 1])
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