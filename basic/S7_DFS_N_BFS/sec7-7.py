import sys
from collections import deque # queue
#sys.stdin = open('input.txt','rt')

max_val = 10000
chk = [0]*(max_val+1)
dist = [0]*(max_val+1)
S,E = map(int,input().split()) # start, end

# starting point
chk[S] = 1
dist[S] = 0

queue = deque()
queue.append(S) # starting point

while queue: # excute if queue is not empty
    now = queue.popleft()
    if now == E:
        break
    for next in(now-1,now+1,now+5): # next = now-1,+1,+5 only
        if 0 < next <= max_val:
            if chk[next] != 1: # except revisit
                queue.append(next)
                chk[next] = 1
                dist[next] = dist[now] + 1

print(dist[E])