import sys
#sys.stdin = open('input.txt','r')

N = int(input())
seq = list(map(int,input().split()))

dy = [0]*N
dy[0] = 1 # initial length

for i in range(1,N):
    maximum = 0 # to find the maximum
    for j in range(i,-1,-1):
        if seq[i] > seq[j] and dy[j] > maximum:
            maximum = dy[j] # maximum update
    dy[i] = maximum + 1 # result update

print(max(dy))
