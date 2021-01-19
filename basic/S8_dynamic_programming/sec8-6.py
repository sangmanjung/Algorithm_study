import sys
#sys.stdin = open('input.txt','r')

N = int(input()) # the number of blocks
B = [] # block

for _ in range(N):
    tmp = list(map(int,input().split()))
    B.append((tmp[0],tmp[1],tmp[2])) # area, height, weight

B.sort(reverse = True) # axis = 'area'

dy = [0]*N
dy[0] = B[0][1] # initial height
result = 0

## the maximum increasing sequence (remember that.)
for i in range(1,N):
    maximum = 0 
    for j in range(i,-1,-1):
        if B[i][2] < B[j][2] and dy[j] > maximum:
            maximum = dy[j]
    dy[i] = maximum + B[i][1]
    if dy[i] > result:
        result = dy[i]

print(result)