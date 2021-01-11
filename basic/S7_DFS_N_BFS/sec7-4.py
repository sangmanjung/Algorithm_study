#import sys
#sys.stdin = open('input.txt','rt')

def DFS(l,s):
    global cnt
    '''
    it may possible that
    
    if s > T:
        return
    '''
    if l == k:
        if s == T:
            cnt += 1
    else:
        '''
        ## The logic of state-space tree in this problem

        'i' is the # of each 'l' coin
        'l' is the value of the coin

        If coins = {5,10,1}, # of each coin = {3,2,5}. Then

        index 0 -> l = 0 -> coins[l] = 5
        and there are cases: 5*0 or 5*1 or ... 5*3
        '''
        for i in range(coin_info[l][1]+1):
            if s < T: # refer to line 7
                DFS(l+1,s+coin_info[l][0]*i)
            else:
                DFS(l+1,s)
                break

if __name__ == '__main__':
    T = int(input())
    k = int(input())
    cnt = 0
    coin_info = []
    for _ in range(k):
        coin_info.append(list(map(int,input().split())))
    DFS(0,0)
    print(cnt)

