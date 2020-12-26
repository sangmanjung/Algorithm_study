import sys
#sys.stdin = open('input.txt','rt')

N,C = map(int,input().split())
coordinates = sorted([int(input()) for _ in range(N)])

## Aim : find the maximum 'distance'
left = 1
right = max(coordinates)-1
result = 0

while left <= right: # binary search
    middle = (left + right)//2

    cnt = 1 # initial count
    first = coordinates[0] # optimal initial value
    for i in range(1,N):
        if abs(coordinates[i] - first) >= middle:
            cnt += 1
            first = coordinates[i] # update

    if cnt >= C:
        result = middle
        left = middle + 1
    else:
        right = middle - 1

print(result)

