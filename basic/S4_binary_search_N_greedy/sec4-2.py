import sys
#sys.stdin = open('input.txt','rt')

K,N = map(int,input().split())
L = [int(input()) for _ in range(K)]


left = 1
right = max(L)
result = 0

while left <= right:
    cnt = 0
    middle = (left + right)//2
    for k in L:
        cnt += k//middle
    if cnt >= N:
        result = middle
        left = middle + 1
    else:
        right = middle - 1

print(result)