n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    ans ^= i - 2
if input() == "Whiteking":
    print("Whiteking" if ans else "Blackking")
else:
    print("Blackking" if ans else "Whiteking")
