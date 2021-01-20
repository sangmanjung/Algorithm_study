import sys
#sys.stdin = open('input.txt','r')

N = int(input())
coins = list(map(int,input().split()))
M = int(input())

dy = [1000]*(M+1)
dy[0] = 0

for i in range(N):
    for j in range(coins[i],M+1):
        dy[j] = min(dy[j],dy[j-coins[i]]+1)

print(dy[M])
