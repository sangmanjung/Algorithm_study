import sys
import heapq as hq # Heap
sys.stdin = open('input.txt','rt')

l = []
## minimum heap
while True:
    N = int(input())
    if N == -1:
        break
    if N == 0:
        if len(l) == 0:
            print(-1)
        else:
            print(hq.heappop(l))
    else:
        hq.heappush(l,N)

## maximum heap
'''
while True:
    N = int(input())
    if N == -1:
        break
    if N == 0:
        if len(l) == 0:
            print(-1)
        else:
            print(-hq.heappop(l))
    else:
        hq.heappush(l,-N)
'''