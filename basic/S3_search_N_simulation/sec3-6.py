import sys
#sys.stdin = open('input.txt','rt')

N = int(input())

L = [0]*N
colsum = []
Ldiags, Rdiags = [],[]

for i in range(N):
    L[i] = list(map(int,input().split()))
    colsum.append(sum(L[i]))
    Ldiags.append(L[i][i])
    Rdiags.append(L[i][(N-1)-i])
diagsum = [sum(Ldiags),sum(Rdiags)]

rowsum = []
for i in range(N):
    s = 0
    for j in range(N):
        s += L[j][i]
    rowsum.append(s)

allsum = rowsum + colsum + diagsum
print(max(allsum))
