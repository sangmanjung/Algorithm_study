import sys
#sys.stdin = open('input.txt','rt')

N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]

def rotation(L,rot,move):
    for i in range(move):
        if rot == 0:
            L.insert(len(L)+1,L[0])
            L.pop(0)
        else:
            L.insert(0,L[-1])
            L.pop(-1)
    return L

M = int(input())
for _ in range(M):
    row,rot,move = map(int,input().split())
    L[row-1] = rotation(L[row-1],rot,move)

s = 0
lt,rt = 0,N
center = N//2
for i in range(N):
    for j in range(lt,rt):
        s += L[i][j]
    if i < center:
        lt += 1
        rt -= 1
    else:
        lt -= 1
        rt += 1
print(s)
