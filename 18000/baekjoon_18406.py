n = input()
left, right = 0, 0
for i in n[:len(n) // 2]:
    left += int(i)
for i in n[len(n) // 2:]:
    right += int(i)
print('LUCKY' if left == right else 'READY')
