import sys
#sys.stdin = open('input.txt','rt')

def DFS(level,sum,totalsum):
    global result
    if sum + (total - totalsum) < result: # Cut-Edge Tech
        return
    if sum > C: # limit of weight
        return
    if level == N:
        if sum > result:
            result = sum
    else:
        DFS(level+1,sum + W[level],totalsum + W[level])
        DFS(level+1,sum,totalsum + W[level])


if __name__ == '__main__':
    C,N = map(int,input().split())
    W = [int(input()) for _ in range(N)]

    result = -2147000000
    total  = sum(W)
    DFS(0,0,0)
    print(result)