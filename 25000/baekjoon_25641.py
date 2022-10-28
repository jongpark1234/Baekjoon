n = int(input())
s = input()
for i in range(n):
    temp = s[i:]
    if temp.count('t') == temp.count('s'):
        print(temp)
        break
