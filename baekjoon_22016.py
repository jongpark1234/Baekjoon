n, k = map(int, input().split())
t = input()
print(t[:k - 1] + t[k - 1:].swapcase())
