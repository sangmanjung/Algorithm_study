import sys
#sys.stdin = open('input.txt','rt')

N,M = map(int,input().split())
weight = sorted(list(map(int,input().split())))

cnt = 0
while weight:
    if len(weight) == 1: # except
        cnt += 1
        break
    if weight[0] + weight[-1] > M:
        cnt += 1
        weight.pop()
    else:
        cnt += 1
        weight.pop(0)
        weight.pop()

print(cnt)

'''
## data structure : deque

from collection impoert deque

Convert the list 'weight' to deque that

weight = deque(weight)
cnt = 0

and just change weight.popleft() == weight.pop(0)
'''