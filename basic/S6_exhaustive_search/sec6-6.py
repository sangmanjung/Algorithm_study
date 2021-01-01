import sys
#sys.stdin = open('input.txt','rt')

def DFS(v):
    global result, cnt
    if v == M:
        for x in result:
            print(x,end = ' ')
        print()
        cnt += 1
    else:
        for i in range(N):
            result[v] = i+1
            DFS(v+1)

if __name__ == '__main__':
    N,M = map(int,input().split())
    result = [0]*M
    cnt = 0
    DFS(0)
    print(cnt)
