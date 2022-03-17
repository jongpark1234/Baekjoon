a = input().split()
if a[0] == 'true':
    a[0] = True
else:
    a[0] = False
if a[2] == 'true':
    a[2] = True
else:
    a[2] = False 
if a[1] == 'OR':
    print(str(a[0] or a[2]).lower())
else:
    print(str(a[0] and a[2]).lower())
