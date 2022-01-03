n = int(input())
left, right = 0, n
while left <= right:
    mid = (left + right) // 2
    if mid ** 2 < n:
        left = mid + 1
    else:
        right = mid - 1
print(left)
