n = int(input())
a = list(map(int, input().split()))
airpods = -1
battery = previous = 0
for i in a:
    if i != airpods:
        airpods = i
        previous = 2
        battery += 2
    else:
        battery += previous << 1
        previous <<= 1
    if battery >= 100:
        battery = 0
        airpods = -1
print(battery)
