import sys
#sys.stdin = open('input.txt','rt')

def DFS(level,sum):
    global result
    if level > result:
        return
    if sum > M:
        return
    if sum == M:
        if level < result:
            result = level
    else:
        for i in range(N):
            DFS(level+1,sum + coins[i])


if __name__ == '__main__':
    N =int(input())
    coins = sorted(list(map(int,input().split())),reverse = True)
    M = int(input())
    result = 2147000000
    DFS(0,0)
    print(result)