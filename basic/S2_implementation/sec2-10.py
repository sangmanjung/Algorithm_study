import sys
#sys.stdin = open('input.txt','rt')

N = int(input())
OX_list = list(map(int,input().split()))

cnt = 0
scores = []
for i in range(N):
    if OX_list[i] == 1:
        cnt += 1
        scores.append(cnt)
    else:
        cnt = 0

print(sum(scores))
