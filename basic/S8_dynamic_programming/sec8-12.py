import sys
#sys.stdin = open('input.txt','r')
'''
## 플로이드 와샬 알고리즘 (그래프 최단거리)
어떤 그래프가 주어질 때 각 i 노드에서 각 j 노드까지 가는 최단거리(최소비용)를 구하는 것.

1.그래프 노드, 엣지, 방향에 주의하여 인접행렬 생성
2.중간에 거쳐가는 노드가 있는 경우 인접행렬에서 그 노드 좌표는 최대값으로 저장
3.i -> j 로 가는 경로와 i -> k -> j 로 가는 경로를 비교해서 최소값을 dy 테이블 값으로 저장
(* i -> k -> t -> j 와 같이 k와 t를 고려할 필요 없음. 루프 돌면서 알아서 1-3-4-5 처럼 경로 다 돌아줌)
4. 3번의 과정을 냅색 알고리즘을 이용하여 갱신해줌
5. 최종적으로 최단거리가 구해진 dy 테이블을 확인한다.
'''

N,M = map(int,input().split())
dy = [[2147000000]*N for _ in range(N)] # 2.

for _ in range(M): # 1.
    node1,node2,edge = map(int,input().split())
    dy[node1-1][node2-1] = edge

for i in range(N): # 1.
    for j in range(N):
        dy[i][i] = 0

# 플로이드 와샬 알고리즘
for k in range(N): # 3.
    for i in range(N): # 4.
        for j in range(N):
            dy[i][j] = min(dy[i][j],dy[i][k] + dy[k][j])

for i in range(N):
    for j in range(N): 
        if dy[i][j] == 2147000000:
            dy[i][j] = 'M'

for i in range(N): # 5.
    for j in range(N):
        print(dy[i][j],end = ' ')
    print()