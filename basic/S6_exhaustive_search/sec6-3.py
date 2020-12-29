import sys
sys.stdin = open('input.txt','rt')

def DFS(x):
    if x == N+1: # stop criterion
        for i in range(1,N+1):
            if check[i] == 1:
                print(i,end = ' ')
        print()
    else:
        check[x] = 1
        DFS(x+1)
        check[x] = 0
        DFS(x+1)

'''
        check[x] = 1
        DFS(x+1)
        check[x] = 0
        DFS(x+1)
        
이 문제는 상태트리를 이용해서 풀면 됨.
(DFS 문제는 일반적으로 상태트리를 잘 짜게 되면 풀림)
check[x] = 1 실행 후 바로 다음의 DFS(x+1)...(1) 실행
-> (1) 내부에서 check[x] = 1 바로 다음의 DFS(x+1)...(2) 실행
이렇게 계속 1로 check 하여 DFS(4)에서 종료 후 다시 이전 단계의 ...(?)로
돌아가서 체크..

'''



if __name__ == '__main__':
    N = int(input())
    check = [0]*(N+1) # cases (1, 2, 3)
    DFS(1) # binary tree (root node = 1)

