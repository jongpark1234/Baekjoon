a = input().split()
b = input()
print(sum(map(lambda x: x.startswith(b) and x != b, a)))
