import sys
sys.stdin = open('input.txt','rt')

def DFS(v, sum):
    if v == N and sum == F:
        for x in p:
            print(x,end = ' ')
        sys.exit(0)
    else:
        for i in range(1,N+1):
            if chk[i] == 0:
                chk[i] = 1
                p[v] = i
                DFS(v+1, sum + (p[v]*b[v]))
                chk[i] = 0

if __name__ == '__main__':
    N,F = map(int,input().split())
    chk = [0]*(N+1)
    p = [0]*N
    cnt = 0
    b = [1]*(N+1)
    for i in range(1,N):
        b[i] = (b[i-1]*(N-i))/i
    DFS(0,0)
