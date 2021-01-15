import sys
from collections import deque
#sys.stdin = open('input.txt','r')

N = int(input())
lattice = [list(map(int,input().split())) for _ in range(N)]

c = (N//2,N//2)
s = lattice[c[0]][c[1]]
queue = deque()
queue.append(c)

L = [(0,1),(1,0),(0,-1),(-1,0)]
chk_matrix = [[0]*N for _ in range(N)]
chk_matrix[c[0]][c[1]] = 1

while queue:
    now = queue.popleft()
    if now[0] == 0 or now[0] == N-1 or now[1] == 0 or now[1] == N-1:
        break
    for x,y in L:
        if chk_matrix[now[0]+x][now[1]+y] == 0:
            s += lattice[now[0]+x][now[1]+y]
            chk_matrix[now[0]+x][now[1]+y] = 1
            queue.append((now[0]+x,now[1]+y))

print(s)