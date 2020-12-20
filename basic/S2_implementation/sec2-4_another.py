import sys
sys.stdin = open('input.txt','rt')

N = int(input())
score = list(map(int,input().split()))
# mean_score = round(sum(score)/N) # round_half_even
ms = sum(score)/N + 0.5
mean_score = int(ms)

diff_min = float('inf')
# finding minimum algorithm
for idx, x in enumerate(score):
    tmp = abs(mean_score-x) # difference
    if tmp < diff_min: # find minimum difference
        diff_min = tmp
        score_min = x # current minimum score
        score_ind = idx + 1 # current index
    elif tmp == diff_min: # if there are several min
        if x > score_min: # choose the bigger one
            score_min = x
            score_ind = idx + 1

print(mean_score,score_ind,sep = ' ')