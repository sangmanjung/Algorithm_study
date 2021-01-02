import sys
#sys.stdin = open('input.txt','rt')

def DFS(v):
    global cnt
    if cnt == 1:
        return
    if v == N:
        s = 0
        for i in range(N):
            s += p[i]*b[i]
        if s == F:
            cnt += 1
            for x in p:
               print(x, end = ' ')
            return
    else:
        for i in range(1,N+1):
            if chk[i] == 0:
                chk[i] = 1
                p[v] = i
                DFS(v+1)
                chk[i] = 0

if __name__ == '__main__':
    N,F = map(int,input().split())
    chk = [0]*(N+1)
    p = [0]*(N)
    cnt = 0
    B = [1,[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],\
        [1,5,10,10,5,1],[1,6,15,20,15,6,1],\
            [1,7,21,35,35,21,7,1],[1,8,28,56,70,56,28,8,1],\
                [1,9,36,84,126,126,84,36,9,1]]
    for x in B:
        if x == 1 and x != N:
            continue
        elif x == 1 and x == N:
            b = x
        if len(x) == N:
            b = x
    DFS(0)
