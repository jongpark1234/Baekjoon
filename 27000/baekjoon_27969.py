ason = input()
print(sum(map(lambda x: 8 if x.isdigit() else 0, ason.split())) + sum(map(lambda x: len(x) + 12 if x.isalpha() else 0, ason.split())) + ason.count('[') * 8)
