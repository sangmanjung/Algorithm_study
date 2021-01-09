#import sys
#sys.stdin = open('input.txt','rt')

def DFS(node):
    global cnt
    if node == nodes:
        cnt += 1 # arrived 'nodes'
    else:
        for j in range(1,nodes+1):
            ## 
            if A[node-1][j-1] == 1 and check[j] == 0:
                check[j] = 1 # visit
                DFS(j) # recursive loop
                check[j] = 0 # back to previous node
        

if __name__ == '__main__':
    nodes, edges = map(int,input().split())
    A = [[0]*nodes for _ in range(nodes)] # Adjacency matrix
    
    for _ in range(edges):
        x,y = map(int,input().split())
        A[x-1][y-1] = 1 # direction graph
    
    check = [0]*(nodes+1) # visited node check
    cnt = 0 # the number of cases: from 1 to nodes

    check[1] = 1 # first visit
    DFS(1)
    print(cnt)