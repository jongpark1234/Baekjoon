temp = 0
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
for i in a:
    temp += i
    if temp in b:
        temp = 0
print(temp)
