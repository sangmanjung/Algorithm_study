import sys
#sys.stdin = open('input.txt','r')

def DFS(x,y):
    if dy[x][y] > 0: # memorization
        return dy[x][y]

    if x == 0 and y == 0:
        return M[0][0]
    else:
        if y == 0:
            dy[x][y] = DFS(x-1,y) + M[x][y]
            return dy[x][y]
        elif x == 0:
            dy[x][y] = DFS(x,y-1) + M[x][y]
            return dy[x][y]
        else:
            dy[x][y] = min(DFS(x-1,y),DFS(x,y-1)) + M[x][y]
            return dy[x][y]

if __name__ == '__main__':
    N = int(input())
    M = [list(map(int,input().split())) for _ in range(N)]

    dy = [[0]*N for _ in range(N)] # for memorization
    print(DFS(N-1,N-1))
