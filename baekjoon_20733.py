from collections import Counter
t = input()
print(Counter([t[len(t) // 3 * i:len(t) // 3 * (i + 1)] for i in range(3)]).most_common(1)[0][0])
