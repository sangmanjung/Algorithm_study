#import sys
#sys.stdin = open('input.txt','rt')

def DFS(l,s):
    global result
    if l == K:
        # since the state-space tree is symmetric,
        if 0 < s <= sum(W):
            result.add(s)
    else:
        DFS(l+1,s + W[l]) # left position
        DFS(l+1,s - W[l]) # right position
        DFS(l+1,s) # not use
    
if __name__ == '__main__':
    K = int(input())
    W = list(map(int,input().split()))
    result = set() # for duplicated result
    DFS(0,0)
    print(sum(W) - len(result))