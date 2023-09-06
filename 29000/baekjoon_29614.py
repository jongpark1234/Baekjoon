credits = {
    'A+': 4.5,
    'B+': 3.5,
    'C+': 2.5,
    'D+': 1.5,
    'A': 4.0,
    'B': 3.0,
    'C': 2.0,
    'D': 1.0,
    'F': 0.0,
}
score = cnt = 0
s = input()
for i in credits:
    cnt += s.count(i)
    score += s.count(i) * credits[i]
    while i in s:
        s = s.replace(i, '')
print(score / cnt)
