## Time limit exceeded (2 / 5 cases)
import sys
#sys.stdin = open('input.txt','rt')

N,M = map(int,input().split())
num = list(map(int,input().split()))

i = 0
while True:
    if i >= N-1:
        break
    if num[i] > num[i+1]:
        num[i],num[i+1] = num[i+1], num[i]
        i = 0
    else:
        i += 1
    if num[i] == M:
        result = i+1

print(result)