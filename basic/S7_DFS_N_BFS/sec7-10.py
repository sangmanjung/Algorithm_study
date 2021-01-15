import sys
#sys.stdin = open('input.txt','r')

dy = [1,0,-1,0]
dx = [0,1,0,-1]

def DFS(x,y):
    global cnt
    if x == 6 and y == 6: # endpoint
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx <= 6 and 0 <= yy <= 6: # barrier
                if maze[xx][yy] == 0:
                    maze[xx][yy] = 1 # visit
                    DFS(xx,yy)
                    maze[xx][yy] = 0 # back

if __name__ == '__main__':
    maze = [list(map(int,input().split())) for _ in range(7)]
    maze[0][0] = 1 # starting point
    cnt = 0
    DFS(0,0)
    print(cnt)

