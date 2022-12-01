n = int(input())
s = input()
print(sum(s[i] != s[n - i - 1] for i in range(n >> 1)))
