import sys
sys.stdin = open('input.txt','rt')

N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]

s = 0
center = N//2
lt = rt = 0
for i in range(N):
    for j in range(lt,rt+1):
        s += L[i][j]
    if i < center:
        lt -= 1
        rt += 1
    else:
        lt += 1
        rt -= 1
        
