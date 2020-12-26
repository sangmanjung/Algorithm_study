import sys
#sys.stdin = open('input.txt','rt')

L = int(input())
B = list(map(int,input().split()))
M = int(input())

for i in range(M):
    mx = max(B)
    mn = min(B)
    cntx = 0
    cntn = 0
    for j in range(L):
        if B[j] == mx:
            cntx += 1
            if cntx == 1:
                B[j] -= 1
        elif B[j] == mn:
            cntn += 1
            if cntn == 1:
                B[j] += 1

print(max(B)-min(B))

