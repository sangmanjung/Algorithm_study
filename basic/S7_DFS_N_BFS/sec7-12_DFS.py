import sys
#sys.stdin = open('input.txt','r')

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def DFS(x,y):
    global cnt
    cnt += 1 # count the house when we visit
    M[x][y] = 0 # check the visited house
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx <= N-1 and 0 <= yy <= N-1:
            if M[xx][yy] == 1:
                DFS(xx,yy) # DFS not work if all houses are visited
                

if __name__ == '__main__':
    N = int(input())
    M = [list(map(int,input())) for _ in range(N)]

    result = []
    # search the starting point
    for i in range(N):
        for j in range(N):
            if M[i][j] == 1:
                cnt = 0 # initialize
                DFS(i,j)
                result.append(cnt)

    print(len(result))
    for r in sorted(result):
        print(r)
