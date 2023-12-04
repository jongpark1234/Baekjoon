n = int(input())
s = input()
print(min(map(lambda x: s.count(x), 'uospc')))
