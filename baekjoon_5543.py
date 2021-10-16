import sys
burgur = []
drink = []
for i in range(3):
    burgur.append(int(sys.stdin.readline()))
for i in range(2):
    drink.append(int(sys.stdin.readline()))
print(min(burgur) + min(drink) - 50)
