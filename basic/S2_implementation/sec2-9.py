import sys
#sys.stdin = open('input.txt','rt')

N = int(input())
reward = []
for i in range(N):
    player = list(map(int,input().split()))
    numlist = list(set(player))
    checklist = [0]*len(numlist)
    for i in range(len(player)):
        for j in range(len(numlist)):
            if player[i] == numlist[j]:
                checklist[j] +=1
    if max(checklist) == 3:
        p = 10000 + \
        (numlist[checklist.index(max(checklist))])\
            *1000
    elif max(checklist) == 2:
        p = 1000 + \
        (numlist[checklist.index(max(checklist))])\
            *100
    else:
        p = max(numlist)*100
    reward.append(p)

print(max(reward))

