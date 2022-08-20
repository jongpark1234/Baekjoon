def backtrack(x, length):
    global result, alist
    if length == 0:
        result.add(x)
        return
    for i in range(26):
        if alist[i]:
            alist[i] -= 1
            backtrack(x + chr(i + 97), length - 1)
            alist[i] += 1
for _ in range(int(input())):
    result = set()
    alist = [0 for _ in range(26)]
    word = input()
    for i in word:
        alist[ord(i) - 97] += 1
    backtrack('', len(word))
    print('\n'.join(sorted(result)))
