cnt = 0
def S(k):
    global cnt
    if k == 1:
        return cnt
    cnt += 1
    return S(k + 1 if k % 2 else k // 2)
print(S(int(input())))
