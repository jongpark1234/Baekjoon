matches = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
for i in [*open(0)][1:]:
    print(sum(matches[j] if j in matches else 0 for j in i.strip()))
