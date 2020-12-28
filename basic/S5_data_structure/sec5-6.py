import sys
from collections import deque
#sys.stdin = open('input.txt','rt')

N,M = map(int,input().split())
danger = deque(list(map(int,input().split())))
num = deque(list(range(N)))

cnt = 0
while danger:
    now = danger[0]
    if all(now >= danger[i] for i in range(1,N)):
        result = num.popleft()
        danger.popleft()
        cnt += 1
        N -= 1
        if result == M:
            print(cnt)
            break
    else:
        danger.append(danger.popleft())
        num.append(num.popleft())