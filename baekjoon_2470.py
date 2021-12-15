from sys import stdin, maxsize
n = int(input())
value = list(map(int, input().split()))
value.sort()
distance = maxsize
l, r = 0, n - 1
while l < r:
    solution = value[l] + value[r]
    if abs(solution) < distance:
        result = [value[l], value[r]]
        distance = abs(solution)
    if solution < 0:
        l += 1
    elif solution > 0:
        r -= 1
    else:
        break
print(*result)
