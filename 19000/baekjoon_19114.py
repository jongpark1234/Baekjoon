ret = 0
n = int(input())
for i in map(int, input().split()):
    ret ^= i + 1 if i & 7 == 7 else i - 1 if i & 7 == 0 else i
print('First' if ret else 'Second')
