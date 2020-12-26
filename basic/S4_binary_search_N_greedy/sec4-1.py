import sys
#sys.stdin = open('input.txt','rt')

N,M = map(int,input().split())
L = sorted(list(map(int,input().split())))

left = 0
right = N
while left <= right:
    middle = (left + right)//2
    if L[middle] == M:
        print(middle+1)
        break
    elif L[middle] < M:
        left = middle + 1
    else:
        right = middle - 1
