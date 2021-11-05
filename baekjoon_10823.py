s = ''
while True:
    try:
        s += input()
    except:
        break
print(sum(map(int, s.split(','))))
