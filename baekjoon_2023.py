n = int(input())
def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def search(num, length):
    if length == n:
        print(num)
        return
    for i in range(1, 10, 2):
        if isprime(num * 10 + i):
            search(num * 10 + i, length + 1)
search(2, 1)
search(3, 1)
search(5, 1)
search(7, 1)
