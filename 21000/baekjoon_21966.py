n = int(input())
s = input()
if n > 25:
    if len(s[11:-11].strip('.').split('.')) > 1:
        print(s[:9] + '......' + s[-10:])
    else:
        print(s[:11] + '...' + s[-11:])
else:
    print(s)
