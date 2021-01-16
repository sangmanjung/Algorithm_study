import sys
import copy
from collections import deque
#sys.stdin = open('input.txt','r')

def BFS(h,M):
    result = []
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    for i in range(N):
        for j in range(N):
            if M[i][j] > h:
                cnt = 1
                M[i][j] = 0
                Q.append((i,j))
                while Q:
                    now = Q.popleft()
                    for k in range(4):
                        x = now[0] + dx[k]
                        y = now[1] + dy[k]
                        if 0 <= x <= N-1 and 0 <= y <= N-1:
                            if M[x][y] > h:
                                cnt += 1
                                M[x][y] = 0
                                Q.append((x,y))
                result.append(cnt)
    return len(result)

if __name__ == '__main__':
    N = int(input())
    M = [list(map(int,input().split())) for _ in range(N)]
    
    C = []
    Q = deque()
    for h in range(1,101):
        new_M = copy.deepcopy(M)
        c = BFS(h,new_M)
        if c == 0:
            break
        else:
            C.append(c)
    print(max(C))
