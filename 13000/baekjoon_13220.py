n = int(input())
a = ''.join(input().split()) * 2
b = ''.join(input().split())
print(['NO', 'YES'][b in a])
