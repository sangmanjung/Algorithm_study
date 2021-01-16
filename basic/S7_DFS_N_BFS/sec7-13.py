import sys
from collections import deque
#sys.stdin = open('input.txt','r')

dx = [-1,0,1,0]
dy = [0,-1,0,1]
Dx = [1,1,-1,-1]
Dy = [1,-1,1,-1]

N = int(input())
M = [list(map(int,input().split())) for _ in range(N)]

cnt = 0
result = []
Q = deque()
for i in range(N):
    for j in range(N):
        if M[i][j] == 1:
            cnt = 1
            M[i][j] = 0
            Q.append((i,j))
            while Q:
                now = Q.popleft()
                for k in range(4):
                    x = now[0] + dx[k]
                    y = now[1] + dy[k]
                    diag_x = now[0] + Dx[k]
                    diag_y = now[1] + Dy[k]
                    if 0 <= x <= N-1 and 0 <= y <= N-1:
                        if M[x][y] == 1:
                            cnt += 1
                            M[x][y] = 0
                            Q.append((x,y))
                    if 0 <= diag_x <= N-1 and 0 <= diag_y <= N-1:
                        if M[diag_x][diag_y] == 1:
                            cnt += 1
                            M[diag_x][diag_y] = 0
                            Q.append((diag_x,diag_y))
            result.append(cnt)

print(len(result))