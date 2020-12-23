import sys
#sys.stdin = open('input.txt','rt')

N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]

s = 0
lm = 1
center = N//2
for i in range(N):
    if center-i >= 0:
        s += sum(L[center-i][0+i:N-i])
    else:
        s += sum(L[center+lm][0+lm:N-lm])
        lm += 1

print(s)