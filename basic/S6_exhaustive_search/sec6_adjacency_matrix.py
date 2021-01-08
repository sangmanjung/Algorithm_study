#import sys
#sys.stdin = open('input.txt','rt')

N,M = map(int,input().split())
A = [[0]*N for _ in range(N)] # Adjacency Matrix

for m in range(M):
    x,y,w = map(int,input().split())
    A[x-1][y-1] = w 

for a in A:
    for i in a:
        print(i,end = ' ')
    print() 