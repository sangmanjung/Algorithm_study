import sys
sys.stdin = open('input.txt','rt')

N = int(input())

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2,end = '')

DFS(N)
