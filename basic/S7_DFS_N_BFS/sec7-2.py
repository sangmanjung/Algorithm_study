#import sys
#sys.stdin = open('input.txt','rt')

def DFS(v,p):
    global result
    if v == N:
        if p > result:
            result = p
    else:
        # binary tree
        if v + Table[v][0] <= N:
            DFS(v+Table[v][0],p+Table[v][1])
        DFS(v+1,p)


if __name__ == '__main__':
    N = int(input())
    Table = []
    for _ in range(N):
        Table.append(list(map(int,input().split())))
    
    result = -2147000000
    DFS(0,0)
    print(result)