from sys import *
n = int(stdin.readline())
deque = []
for _ in range(n):
    command = stdin.readline().split()
    if command[0] == 'push_front':
        deque.insert(0, command[1])
    elif command[0] == 'push_back':
        deque.insert(len(deque), command[1])
    elif command[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            del deque[0]
    elif command[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[len(deque) - 1])
            del deque[len(deque) - 1]
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif command[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[len(deque) - 1])
