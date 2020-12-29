import sys
sys.stdin = open('input.txt','rt')

def DFS(v): # basic structure of DFS
    if v > 7:
        return
    else:
        print(v,end = ' ') # visit
        DFS(v*2) # left children
        DFS(v*2+1) # right children

if __name__ == '__main__':
    DFS(1)