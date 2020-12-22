import sys
#sys.stdin = open('input.txt','rt')

N,M = map(int,input().split())
A = list(map(int,input().split()))

cnt = 0
for i in range(N):
    for j in range(N-i,0,-1):
        s = sum(A[i:N-j+1])
        if s == M:
            cnt += 1

print(cnt)

