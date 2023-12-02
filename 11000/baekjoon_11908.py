n = int(input())
cards = list(map(int, input().split()))
print(sum(cards) - max(cards))
