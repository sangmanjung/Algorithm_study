import sys
#sys.stdin = open('input.txt','r')

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def DFS(x,y):
    global cnt
    if x == end[0] and y == end[1]:
        cnt += 1
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx <= N-1 and 0 <= yy <= N-1:
                if M[x][y] < M[xx][yy]:
                    DFS(xx,yy)

if __name__ == '__main__':
    N = int(input())
    M = [list(map(int,input().split())) for _ in range(N)]
    
    s = 2147000000
    e = -2147000000
    for i in range(N):
        for j in range(N):
            if s >= M[i][j]:
                s,start = M[i][j],(i,j)
            if e <= M[i][j]:
                e, end = M[i][j],(i,j)

    cnt = 0
    DFS(start[0],start[1])
    print(cnt)