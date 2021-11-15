while True:
    strlist = []
    s = input().lower()
    if s == '#': break
    for i in s:
        if i not in strlist and i.isalpha():
            strlist.append(i)
    print(len(strlist))
