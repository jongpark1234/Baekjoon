a = input()
b = input()
c = input()
temp = int(a) + 3 if a.isdigit() else int(b) + 2 if b.isdigit() else int(c) + 1
print('FizzBuzz' if temp % 3 == 0 and temp % 5 == 0 else 'Fizz' if temp % 3 == 0 else 'Buzz' if temp % 5 == 0 else temp)
