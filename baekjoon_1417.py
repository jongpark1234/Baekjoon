cnt = 0
vote = [int(input()) for _ in range(int(input()))]
while vote[0] != max(vote) or vote.count(max(vote)) != 1:
    cnt += 1
    vote[vote.index(max(vote), 1, len(vote))] -= 1
    vote[0] += 1
print(cnt)
