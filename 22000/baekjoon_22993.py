n = int(input())
a = list(map(int, input().split()))
result = a[0]
for i in sorted(a[1:]):
    if result > i:
        result += i
    else:
        print('No')
        exit()
print('Yes')
