n = input()
f = int(input())
for i in range(100):
    if int(n[:-2] + str(i).zfill(2)) % f == 0:
        print(str(i).zfill(2))
        break
