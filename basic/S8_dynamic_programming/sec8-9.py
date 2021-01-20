import sys
#sys.stdin = open('input.txt','r')

types, weight = map(int,input().split())

V = []
for _ in range(types):
    V.append(list(map(int,input().split())))

dy = [0]*(weight+1)

result = 0
for i in range(types):
    for j in range(V[i][0],weight+1):
        tmp = dy[j-V[i][0]] + V[i][1]
        if tmp > dy[j]:
            dy[j] = tmp
        if dy[j] > result:
            result = dy[j]

print(result) # result 불필요
# print(dy[weight]) 로 충분

'''
## 불필요한 코드 줄이기

for _ in range(types):
    w,v = map(int,input().split())
    for j in range(w,weight+1):
        dy[j] = max(dy[j],dy[j-w]+v)

'''