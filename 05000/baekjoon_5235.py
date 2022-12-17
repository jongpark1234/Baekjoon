for _ in range(int(input())):
    numlist = list(map(int, input().split()))[1:]
    even = sum([i for i in numlist if ~i & 1])
    odd = sum([i for i in numlist if i & 1])
    print('ODD' if odd > even else 'EVEN' if odd < even else 'TIE')
