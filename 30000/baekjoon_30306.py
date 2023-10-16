result = 0
n = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
for i in first:
    for j in second:
        if i > j:
            result += 1
        elif i < j:
            result -= 1
print('first' if result > 0 else 'second' if result < 0 else 'tie')
