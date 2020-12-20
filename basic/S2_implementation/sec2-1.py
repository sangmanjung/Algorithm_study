#import sys
#sys.stdin = open('input.txt','rt')

N,K = map(int,input().split())

numlist = []
for i in range(1,N+1):
    if N % i == 0:
        numlist.append(i)

if len(numlist) >= K:
    print(numlist[K-1])
else:
    print(-1)
