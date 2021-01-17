import sys
#sys.stdin = open('input.txt','r')

def DFS(x,y):
    global result
    check[x][y] = 1
    if x == 9:
        if M[x][y] == 2:
            result = True
    else:        
        if y+1 < 10 and M[x][y+1] == 1 and check[x][y+1] == 0:
            DFS(x,y+1)
        elif y-1 >= 0 and M[x][y-1] == 1 and check[x][y-1] == 0:
            DFS(x,y-1)
        else:
            DFS(x+1,y)
                
if __name__ == '__main__':
    M = [list(map(int,input().split())) for _ in range(10)]
    
    result = False
    for j in range(10):
        check = [[0]*10 for _ in range(10)]
        if M[0][j] == 1:
            DFS(0,j)
            if result == True:
                print(j)
                break
            

