a = input()
if int(a) < 100:
    print(int(a[0]) + int(a[1]))
elif int(a) < 1000:
    if int(a[1]) == 0:
        print(10 + int(a[2]))
    else:
        print(10 + int(a[0]))
else:
    print(20)
