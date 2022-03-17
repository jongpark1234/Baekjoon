nums = [0, 0]
for i in map(int, input().split()):
    nums[i - 1] += 1
print(1 if nums[0] > nums[1] else 2)
