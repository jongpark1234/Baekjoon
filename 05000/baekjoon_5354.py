for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print('#')
    elif n == 2:
        print('##\n##')
    else:
        print('#' * n)
        for _ in range(n - 2):
            print('#' + 'J' * (n - 2) + '#')
        print('#' * n)
    print()
