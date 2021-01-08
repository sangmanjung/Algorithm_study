#import sys
#sys.stdin = open('input.txt','rt')

def DFS(L,s):
    global cnt
    if L == K:
        combsum = sum(result)
        if combsum % M == 0:
            cnt += 1
    else:
        for j in range(s,N+1):
            result[L] = nums[j-1]
            DFS(L+1,j+1) 

if __name__ == '__main__':
    N,K = map(int,input().split())
    nums = list(map(int,input().split()))
    M = int(input())

    result = [0]*(N+1)
    cnt = 0
    DFS(0,1)
    print(cnt)