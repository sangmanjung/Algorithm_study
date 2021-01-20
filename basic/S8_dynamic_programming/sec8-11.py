import sys
#sys.stdin = open('input.txt','r')

N,M = map(int,input().split())

dy =[0]*(M+1)

# 냅색 알고리즘 기본 구조
for i in range(1,N+1):
    score,times = map(int,input().split()) # 중복 허용하지 않을때 순서 거꾸로
    for j in range(M,times-1,-1):
        dy[j] = max(dy[j],dy[j-times] + score)

print(dy[M])