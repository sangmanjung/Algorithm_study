import sys
#sys.stdin = open('input.txt','rt')

N = int(input())
Nlist = list(map(int,input().split()))
M = int(input())
Mlist = list(map(int,input().split()))

mergeList = [0]*(N+M)

ind = 0
p1,p2 = 0,0
while True:
    if p1 == N:
        mergeList[ind:] = Mlist[p2:]
        break
    elif p2 == M:
        mergeList[ind:] = Nlist[p1:]
        break
    if Nlist[p1] <= Mlist[p2]:
        mergeList[ind] = Nlist[p1]
        ind += 1
        p1 += 1
    else:
        mergeList[ind] = Mlist[p2]
        ind += 1
        p2 += 1

for elem in mergeList:
    print(elem, end =' ')
    