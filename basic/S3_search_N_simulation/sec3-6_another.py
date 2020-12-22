import sys
#sys.stdin = open('input.txt','rt')

N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]

max_val = -2147000000 # initial value

## find the maximum: row, column
for i in range(N):
    s1 = s2 = 0 # row, col (initialize)
    for j in range(N):
        s1 += L[i][j]
        s2 += L[j][i]
    if s1 > max_val:
        max_val = s1
    if s2 > max_val:
        max_val = s2

s1 = s2 = 0 # initialization for 2 diagonal sum

## find the maximum: 2 diagonal
for i in range(N): 
    s1 += L[i][i]
    s2 += L[i][(N-1)-i]
if s1 > max_val:
    max_val = s1
if s2 > max_val:
    max_val = s2

print(max_val)
