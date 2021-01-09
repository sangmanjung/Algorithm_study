#import sys
#sys.stdin = open('input.txt','rt')

def DFS(v,s,t): # == find the # of subsets
    global result
    if t > M: # time limit
        return
    if v == N:
        if s > result:
            result = s
    else:
        # binary tree
        DFS(v+1,s+p[v][0],t+p[v][1]) # select
        DFS(v+1,s,t) # not select

if __name__ == '__main__':
    N,M = map(int,input().split())
    p = []
    for _ in range(N):
        p.append(list(map(int,input().split())))

    result = -2147000000
    DFS(0,0,0)
    print(result)
    