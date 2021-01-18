import sys
#sys.stdin = open('input.txt','r')

## Top-Down DP
def DFS(l):
    if dy[l] > 0: # cut-edge technique
        return dy[l]

    if l == 1 or l == 2:
        return l
    else:
        dy[l] = DFS(l-1)+DFS(l-2) # dy에 기록을 하므로 memorization
        return dy[l]


if __name__ == '__main__':
    N = int(input())
    dy = [0]*(N+1) # the # of methods of cutting line
    print(DFS(N))