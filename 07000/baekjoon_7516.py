for i in range(int(input())):
    result = 1
    n = int(input())
    for j in range(2, int(n ** 0.5) + 1):
        cnt = 0
        while not n % j:
            n //= j
            cnt += 1
        result *= cnt * 2 + 1
    if n > 1:
        result *= 3
    print(f'Scenario #{i + 1}:\n{result // 2 + 1}\n')
