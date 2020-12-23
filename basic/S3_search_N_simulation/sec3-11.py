import sys
#sys.stdin = open('input.txt','rt')

L = [list(map(int,input().split())) for _ in range(7)]

def solution(L):
    cnt = 0
    for i in range(7):
        for j in range(3): # moving
            tmp = L[i][j:5+j]
            '''
            ## Note:
            check tmp == tmp[::-1] alternatively.
            '''
            if all(tmp[0+k] == tmp[4-k] for k in range(2)):
                cnt += 1
    return cnt

# change the position
change_L = [[0]*7 for _ in range(7)]
for j in range(7):
    for i in range(7):
        change_L[j][i] = L[i][j]

print(solution(L) + solution(change_L))
