from sys import stdin
MAX = 100000
fibonacci: list[int] = [1, 1]
strFibonacci: list[list] = [[], [['1', 0], ['1', 1]]] + [[] for _ in range(MAX // 10 - 2)]
for i in range(2, MAX):
    n = sum(fibonacci[-2:])
    if (len(str(n)) > 100):
        n //= 10
        fibonacci[-1] //= 10
    fibonacci.append(n)
    front = str(n)[:40]
    idx = int(front[:4])
    for j in range(5):
        strFibonacci[idx // (10 ** j)].append([front, i])
for tc in range(int(input())):
    front = stdin.readline().rstrip()
    idx = int(front[:4])
    print(f'Case #{tc + 1}:', end=' ')
    for i in strFibonacci[idx]:
        if front == str(i[0])[:len(front)]:
            print(i[1])
            break
    else:
        print(-1)
