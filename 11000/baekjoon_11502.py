from sys import stdin
def isprime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
seive = [i for i in range(2, 1001) if isprime(i)]
for _ in range(int(stdin.readline())):
    found = False
    num = int(stdin.readline())
    for i in seive:
        for j in seive:
            for k in seive:
                if i + j + k == num:
                    print(i, j, k)
                    found = True
                    break
            if found:
                break
        if found:
            break
    if not found:
        print(0)
