import sys
#sys.stdin = open('input.txt','r')

# DFS 조합 문제에 피자배달거리만 추가해서 구해주면 되는 문제
def DFS(l,s):
    global result
    if l == M:
        city_dist = 0
        for h in house:
            x1 = h[0]
            y1 = h[1]
            pizza_dist = 2147000000 # to find minimum pizza_dist
            for c in cbn:
                x2 = pizza[c][0]
                y2 = pizza[c][1]
                pizza_dist = min(pizza_dist,abs(x1-x2)+abs(y1-y2))
            city_dist += pizza_dist

        if city_dist < result:
            result = city_dist

    else: # 여기까지는 combination problem
        for k in range(s,len(pizza)):
            cbn[l] = k
            DFS(l+1,k+1)

if __name__ == '__main__':
    N,M = map(int,input().split())
    city = [list(map(int,input().split())) for _ in range(N)]

    cbn = [0]*M
    result = 2147000000 # to find minimum city_dist
    house,pizza = [],[]

    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                house.append((i,j))
            if city[i][j] == 2:
                pizza.append((i,j))
    
    DFS(0,0)
    print(result)
