import sys
from collections import deque
#sys.stdin = open('input.txt','rt')

N,K = map(int,input().split())
queue = deque([x for x in range(1,N+1)])

i = 0
while len(queue) > 1:
    if i == K:
        for _ in range(i-1):
            queue.append(queue.popleft())
        queue.popleft()
        i = 0
    else:
        i += 1
    
print(queue[0])