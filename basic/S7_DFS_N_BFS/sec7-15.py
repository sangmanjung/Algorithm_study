import sys
from collections import deque
#sys.stdin = open('input.txt','r')

dx = [-1,0,1,0]
dy = [0,-1,0,1]

M,N = map(int,input().split())
Box = [list(map(int,input().split())) for _ in range(N)]
days = [[0]*M for _ in range(N)] 

Q = deque()
for i in range(N):
    for j in range(M):
        if Box[i][j] == 1:
            Q.append((i,j)) # 익은 감 초기값을 따로 저장
            '''
            하나 저장하고 바로 BFS 수행하면
            해당 단계의 모든 익은 감 동시다발적으로 체크 못함
            '''
result = 0 # 모든 유닛이 1 (익은감)인 경우 자연스럽게 0 호출됨
while Q:
    now = Q.popleft()
    for k in range(4):
        x = now[0] + dx[k]
        y = now[1] + dy[k]
        if 0 <= x <= N-1 and 0 <= y <= M-1 and Box[x][y] == 0:
            Box[x][y] = 1
            # 상태 트리의 레벨로 찾으려면 부모값에 더해줘야함
            days[x][y] = days[now[0]][now[1]] + 1
            if days[x][y] > result:
                result = days[x][y] # 최대값 찾기
            Q.append((x,y))

check = 0
for i in range(N):
    for j in range(M):
        if Box[i][j] == 0:
            check = 1 # 감이 모두 익지 못하는 상황
            break
if check == 1:
    print(-1) # output
else:
    print(result) # output
