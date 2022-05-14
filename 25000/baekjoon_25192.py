from sys import stdin
result = 0
sent = set()
for _ in range(int(input())):
    msg = stdin.readline().rstrip()
    if msg == 'ENTER':
        result += len(sent)
        sent = set()
    else:
        sent.add(msg)
print(result + len(sent))
