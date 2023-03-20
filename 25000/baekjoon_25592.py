turn = 1
n = int(input())
while turn <= n:
    n -= turn
    turn += 1
print(turn - n if turn & 1 else 0)
