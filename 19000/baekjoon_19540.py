n = int(input())
print(1, 3)
print(2, 3)
print(3, 4)
print(4, 5)
for i in [[[5, 6]], [[4, 6], [6, 7]], [[5, 6], [5, 7], [7, 8]], [[1, 6], [2, 7], [3, 8], [8, 9]], [[5, 6], [4, 7], [7, 8], [4, 9], [9, 10]], [[1, 6], [3, 7], [7, 8], [8, 9], [9, 10], [10, 11]]][n % 6]:
    print(*i)
i = n % 6 + 6
while i < n:
    print(i, i + 1)
    print(i, i + 3)
    print(i, i + 5)
    print(i + 1, i + 2)
    print(i + 3, i + 4)
    print(i + 5, i + 6)
    i += 6