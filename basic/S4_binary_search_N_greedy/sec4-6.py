import sys
#sys.stdin = open('input.txt','rt')

N = int(input())

cand = []
for _ in range(N):
    h,w = map(int,input().split())
    cand.append((h,w))

cand.sort(reverse = True)

cnt = 0
H = W = 0
for h,w in cand:
    if h > H or w > W:
        H = h # not necessary (sorting -> height)
        W = w
        cnt += 1
print(cnt)
