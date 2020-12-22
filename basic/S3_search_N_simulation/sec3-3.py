import sys
#sys.stdin = open('input.txt','rt')

cards = list(range(1,21))

for _ in range(10):
    left,right = map(int,input().split())
    while True:
        if left >= right:
            break
        else:
            cards[left-1],cards[right-1] = cards[right-1],cards[left-1]
            left += 1
            right -= 1

for c in cards:
    print(c, end = ' ')
    