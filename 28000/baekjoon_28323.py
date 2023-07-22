result = 1
n = int(input())
a = list(map(int, input().split()))
flag = a[0] & 1
for i in a[1:]:
    if i & 1 ^ flag:
        result += 1
        flag ^= 1
print(result)
