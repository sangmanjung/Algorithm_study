import sys
#sys.stdin = open('input.txt','rt')

def DFS(v):
    global cnt
    if v == M:
        for j in range(M):
            print(result[j],end = ' ')
        print()
        cnt += 1
    else:
        for i in range(1,N+1):
            if check[i] == 0:
                check[i] = 1
                result[v] = i
                DFS(v+1)
                check[i] = 0


if __name__ == '__main__':
    N,M = map(int,input().split())
    result = [0]*M
    check = [0]*(N+1)
    cnt = 0
    DFS(0)
    print(cnt)