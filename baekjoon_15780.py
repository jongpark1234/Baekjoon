n, k = map(int, input().split())
multitap = list(map(int, input().split()))
sphere = 0
for i in multitap:
    sphere += i // 2 + 1 if i % 2 else i // 2
print('NO' if n > sphere else 'YES')
