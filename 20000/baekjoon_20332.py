n = int(input())
print('no' if sum(map(int, input().split())) % 3 else 'yes')
