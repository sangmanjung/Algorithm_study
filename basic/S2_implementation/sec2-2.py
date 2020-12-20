T = int(input())

for t in range(T):
    N,s,e,k = map(int,input().split())
    numList = list(map(int,input().split()))
    L = sorted(numList[s-1:e])
    print('#%d %d' % (t+1,L[k-1]))

