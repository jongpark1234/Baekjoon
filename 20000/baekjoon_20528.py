wrong = False
n = int(input())
words = [i[0] for i in list(input().split())]
for i in range(len(words) - 1):
    if words[i] != words[i + 1]:
        wrong = True
        break
print(0 if wrong else 1)
