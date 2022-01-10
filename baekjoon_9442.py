from sys import stdin
year = 0
while True:
    try:
        year += 1
        a, b = input().split()
        words = [input() for _ in range(int(a))]
        new_words = []
        for i in range(int(a)):
            s = ''
            for j in words[i]:
                s += chr(b.index(j) + 65)
            new_words.append([s, i])
        print(f'year {year}')
        for i in sorted(new_words):
            print(words[i[1]])
    except ValueError:
        break
