from sys import stdin
def isprime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def ispalindrome(num):
    if num == num[::-1]:
        return True
    return False
a, b = map(int, stdin.readline().split())
if b > 10e6:
    b = int(10e6)
palindroms = [num for num in range(a, b + 1) if ispalindrome(str(num))] 
primes = [str(num) for num in palindroms if isprime(num)]
if primes:
    print('\n'.join(primes))
print(-1)
