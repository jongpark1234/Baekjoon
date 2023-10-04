n = int(input())
temp = sum(map(int, input().split()))
print(['Left', 'Stay', 'Right'][sum(eval(f'temp >{i}0') for i in ' =')])
