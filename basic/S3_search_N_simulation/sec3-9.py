import sys
#sys.stdin = open('input.txt','rt')

N = int(input())
L = [[0]*(N+2) for _ in range(N+2)]

for i in range(1,N+1):
    L[i][1:N+1] = list(map(int,input().split()))

cnt = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if L[i][j] > L[i][j+1]:
            if L[i][j] > L[i][j-1]:
                if L[i][j] > L[i+1][j]:
                    if L[i][j] > L[i-1][j]:
                        cnt += 1
print(cnt)

'''
## Note: use the function all()
Let the direction list dx, dy are as

dx = [-1, 0, 1, 0] # left & right,
dy = [0, 1, 0, -1] # lower & upper.

Then,

for i in range(1,N+1):
    for j in range(1,N+1):
        if all(L[i][j] > L[i+dx[k]][i+dy[k]] for k in range(4))
            cnt += 1

has the same result above.
'''