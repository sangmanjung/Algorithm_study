#import sys
#sys.stdin = open('input.txt','rt')

N = int(input())
score = list(map(int,input().split()))
mean_score = round(sum(score)/N)

diff = []
for i in range(N):
    diff.append(abs(mean_score - score[i]))

near_score = []
for tup in enumerate(diff):
    if tup[1] == min(diff):
        near_score.append(score[tup[0]])

print(mean_score,score.index(max(near_score))+1,sep = ' ')
