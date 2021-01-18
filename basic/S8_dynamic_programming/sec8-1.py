import sys
#sys.stdin = open('input.txt','r')

## Bottom-Up DP

N = int(input())
dy = [0]*(N+1) # the # of methods of cutting line

 # initial value for dynamic programming
dy[1] = 1
dy[2] = 2

for i in range(3,N+1):
    dy[i] = dy[i-1] + dy[i-2] # recurrence relation

print(dy[N])