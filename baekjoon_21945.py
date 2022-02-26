temp = 0
n = int(input())
for i in input().split():
    if i == i[::-1]:
        temp += int(i)
print(temp)
