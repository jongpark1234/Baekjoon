import re
n = int(input())
print(len(re.findall(r'\b(she|her|he|him)\b', input())))
