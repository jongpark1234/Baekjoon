from datetime import datetime
date = datetime(*map(int, input().split('-')))
print(sum(datetime(*map(int, input().split('-'))) >= date for _ in range(int(input()))))
