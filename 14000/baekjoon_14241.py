from collections import deque
input()
score = 0
slime = deque(sorted(list(map(int, input().split())), reverse=True))
while len(slime) != 1:
    newslime = slime[0] + slime[1]
    score += slime[0] * slime[1]
    slime.popleft()
    slime.popleft()
    slime.appendleft(newslime)
print(score)
