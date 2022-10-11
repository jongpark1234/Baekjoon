numlist = []
n = int(input())
p = int(input())
if n < 5:
    numlist.append(p)
else:
    if n >= 5:
        numlist.append(max(0, p - 500))
    if n >= 10:
        numlist.append(int(p * 0.9))
    if n >= 15:
        numlist.append(max(0, p - 2000))
    if n >= 20:
        numlist.append(int(p * 0.75))
print(min(numlist))
