import sys
#sys.stdin = open('input.txt','rt')

N = int(input())
L = list(map(int,input().split()))

seq = [0]*N
for i in range(N):
    for j in range(N):
        if L[i] == 0 and seq[j] == 0:
            seq[j] = i+1
            break
        elif seq[j] == 0:
            L[i] -= 1 
            '''
            # if L[i] = 5, i = 0, then
            check seq[j] == 0 until L[.] = 0
            After that, check seq[j] == 0
            and insert i+1.
            '''
for x in seq:
    print(x,end=' ')