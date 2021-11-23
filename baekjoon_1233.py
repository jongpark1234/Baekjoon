from collections import Counter
s1, s2, s3 = map(int, input().split())
eyes = []
for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            eyes.append(i + j + k)
print(Counter(eyes).most_common(1)[0][0])
