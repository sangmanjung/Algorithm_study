## Time limit exceeded (all test cases are passed but)
import sys
#sys.stdin = open('input.txt','rt')

def DFS(v):
    global s
    if v == N+1:
        tmp = []
        for i in range(1,N+1):
            if check[i] == 1:
                tmp.append(W[i-1])
        s.append(sum(tmp))
    else:
        check[v] = 1
        DFS(v+1)
        check[v] = 0
        DFS(v+1)
    return s

if __name__ == '__main__':
    C,N = map(int,input().split())
    W = [int(input()) for _ in range(N)]
    
    s = []
    check = [0]*(N+1)
    
    result = sorted(DFS(1),reverse = True)
    for x in result:
        if x <= C:
            print(x)
            break
    
