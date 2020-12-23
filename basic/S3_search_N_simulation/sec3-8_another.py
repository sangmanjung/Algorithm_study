import sys
#sys.stdin = open('input.txt','rt')

N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]

M = int(input())
for _ in range(M):
    row,rot,move = map(int,input().split())
    for i in range(move):
        if rot == 0:
            L[row-1].append(L[row-1].pop(0))
        else:
            L[row-1].insert(0,L[row-1].pop())

s = 0
lt,rt = 0,N
for i in range(N):
    for j in range(lt,rt):
        s += L[i][j]
    if i < N//2:
        lt += 1
        rt -= 1
    else:
        lt -= 1
        rt += 1
print(s)
