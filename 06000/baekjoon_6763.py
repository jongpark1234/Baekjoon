limit = int(input())
speed = int(input())
over = speed - limit
fine = 100 if 0 < over < 21 else (270 if 20 < over < 31 else 500)
if over > 0:
    print(f'You are speeding and your fine is ${fine}.')
else:
    print('Congratulations, you are within the speed limit!')
