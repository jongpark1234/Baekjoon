numlist = {int(input()) for _ in range(int(input()))}
seq = {i for i in range(1, max(numlist) + 1)} - numlist
print('\n'.join(map(str, sorted(seq))) if seq else 'good job')
