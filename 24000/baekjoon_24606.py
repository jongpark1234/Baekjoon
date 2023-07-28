s1 = input()
s2 = input()
print(1 << sum(s1[i] != s2[i] for i in range(4)))
