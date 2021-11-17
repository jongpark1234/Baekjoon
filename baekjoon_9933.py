passwords = [input() for i in range(int(input()))]
for i in passwords:
    if i[::-1] in passwords:
        print(len(i), i[len(i) // 2])
        break
