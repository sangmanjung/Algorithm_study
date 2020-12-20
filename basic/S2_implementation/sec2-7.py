import sys
#sys.stdin = open('input.txt','rt')

N = int(input())
check = [0]*(N+1)
cnt = 0
for i in range(2,N+1):
    if check[i] == 0:
        cnt += 1
        for j in range(i,N+1,i):
            check[j] = 1

print(cnt)