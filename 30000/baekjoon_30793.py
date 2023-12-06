vx = eval(input().replace(*' /'))
print('weak' if vx < 0.2 else 'normal' if vx < 0.4 else 'strong' if vx < 0.6 else 'very strong')
