import sys
#sys.stdin = open('input.txt','rt')

N,M = map(int,input().split())
A = list(map(int,input().split()))

s = A[0]
cnt = 0
left,right = 0,1
while True: # O(n)
    if s < M: # the summation is too small
        if right < N: # searching limit
            s += A[right] 
            right += 1
        else:
            break
    elif s == M: # check
        cnt += 1
        # it is done for current start point of A
        s -= A[left]
        left += 1
    else: # the summation is too large
        # it is done for current start point of A
        s -= A[left]
        left += 1

print(cnt)
