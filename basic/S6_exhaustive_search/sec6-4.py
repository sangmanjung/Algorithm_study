import sys
#sys.stdin = open('input.txt','rt')

def DFS(v):
    global cnt
    if v == N+1:
        tmp1, tmp2 = [], []
        for i in range(1,N+1):
            if check[i] == 1:
                tmp1.append(elem[i-1])
            else:
                tmp2.append(elem[i-1])
        if sum(tmp1) == sum(tmp2):
            cnt += 1
    else:
        check[v] = 1
        DFS(v+1)
        check[v] = 0
        DFS(v+1)
    return cnt

if __name__ == '__main__':
    N = int(input())
    elem = list(map(int,input().split()))
    
    cnt = 0
    check = [0]*(N+1)

    if DFS(1) != 0:
        print('YES')
    else:
        print('NO')
