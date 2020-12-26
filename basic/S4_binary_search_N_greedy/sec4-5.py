import sys
#sys.stdin = open('input.txt','rt')

N = int(input())
use_rooms = []
for _ in range(N):
    a,b = map(int,input().split())
    use_rooms.append((a,b))

# choose the end time since we want to have the max_num of rooms
use_rooms.sort(key = lambda x: (x[1],x[0]))

cnt = 1 # initial count
ep = use_rooms[0][1] # optimal initial value
for i in range(1,N):
    if ep <= use_rooms[i][0]:
        cnt += 1
        ep = use_rooms[i][1] # update

print(cnt)