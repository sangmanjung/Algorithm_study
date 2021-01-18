import sys
#sys.stdin = open('input.txt','r')

## Top-Down DP
def DFS(l):
    if dy[l] > 0:
        return dy[l]
    if l == 1 or l == 2:
        return l
    else:
        dy[l] = DFS(l-1) + DFS(l-2)
        return dy[l]

if __name__ == '__main__':
    N = int(input())
    dy = [0]*(N+1)

'''
## Bottom-Up DP

N = int(input())
dy = [0]*(N+1)

dy[0] = 1
dy[1] = 2

for i in range(3,N+1):
    dy[i] = dy[i-1] + dy[i-2]

print(dy[N])
'''