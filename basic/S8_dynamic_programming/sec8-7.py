import sys
#sys.stdin = open('input.txt','r')

N = int(input())
M = [list(map(int,input().split())) for _ in range(N)]

dy = [[0]*N for _ in range(N)] # dynamic programming array
dy[0][0] = M[0][0] # starting point

for i in range(1,N):
    dy[0][i] = dy[0][i-1] + M[0][i] # initial columns
    dy[i][0] = dy[i-1][0] + M[i][0] # initial rows

for i in range(1,N):
    for j in range(1,N):
        # dy[i][j] = min(dy[i-1][j],dy[i][j-1]) + M[i][j] is also possible
        x = dy[i-1][j] + M[i][j] # down
        y = dy[i][j-1] + M[i][j] # right
        if x >= y:
            dy[i][j] = y
        else:
            dy[i][j] = x

print(dy[N-1][N-1])

'''
# 결과 확인용
for t in dy:
    print(t,end = '\n')
print()
'''

'''
## Greedy 로 푼 경우 답이 틀림 (최적해를 찾지 못했음)

x,y = 0,0
result = M[0][0]

while True:
    if x == N-1:
        break
    if 0 <= y+1 <= N-1 and M[x+1][y] > M[x][y+1]:
        result += M[x][y+1]
        y += 1
    else:
        result += M[x+1][y]
        x += 1
print(result)
'''

