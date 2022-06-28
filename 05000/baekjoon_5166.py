p = [0 for _ in range(26)]
for i in range(int(input())):
    result = 0
    n, m, s = map(float, input().split())
    n = int(n)
    m = int(m)
    for j in range(m):
        char, temp = input().split()
        p[ord(char) - 97] = float(temp)
    for j in range(n):
        word = input()
        temp = 1
        for k in range(len(word)):
            temp *= p[ord(word[k]) - 97]
        temp *= s
        result += temp
    data = format(result, 'e')
    data = data[:6] + data[-4:].upper()
    print(f'Data Set {i + 1}:\n{data}\n')
