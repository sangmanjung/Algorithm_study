import sys
from collections import deque
#sys.stdin = open('input.txt','r')

lattice = [list(map(int,input().split())) for _ in range(7)]
lattice[0][0] = 1
dist = [[0]*7 for _ in range(7)] # 헤맨 이유: dist를 만들어서 check 안했음.

dx = [1,-1,0,0]
dy = [0,0,1,-1]

queue = deque()
queue.append((0,0))

while queue:
    Qsize = len(queue)
    for _ in range(Qsize):
        now = queue.popleft()
        for i in range(4):
            x = now[0] + dx[i]
            y = now[1] + dy[i]
            if 0 <= x <= 6 and 0 <= y <= 6:
                if lattice[x][y] == 0:
                    queue.append((x,y))
                    lattice[x][y] = 1 # 여기까지는 동일하게 작성
                    dist[x][y] = dist[now[0]][now[1]] + 1 # dist로 check 안함

if dist[6][6] > 0:
    print(dist[6][6])
else:
    print(-1)