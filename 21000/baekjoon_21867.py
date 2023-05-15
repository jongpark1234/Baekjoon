import re
n = int(input())
s = re.sub(r'J|A|V', '', input())
print(s if s else 'nojava')
