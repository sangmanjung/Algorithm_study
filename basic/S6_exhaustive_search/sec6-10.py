import sys
#sys.stdin = open('input.txt','rt')

def DFS(v,s):
    global cnt
    if v == M:
        for i in range(M):
            print(result[i],end = ' ')
        cnt += 1
        print()
    else:
        for i in range(s,N+1):
            '''
            L : n choose k의 k
            s : 중복 제거용
            j : 가지 탐색용 (선택할 값)
            '''
            result[v] = i
            DFS(v+1,i+1)

if __name__ == '__main__':
    N,M = map(int,input().split())
    ck = [0]*(N+1)
    result = [0]*M
    cnt = 0
    DFS(0,1)
    print(cnt)
