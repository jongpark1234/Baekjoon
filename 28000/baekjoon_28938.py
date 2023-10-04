n = int(input())
temp = sum(map(int, input().split()))
print(['Left', 'Stay', 'Right'][sum(temp >= i for i in range(2))])
