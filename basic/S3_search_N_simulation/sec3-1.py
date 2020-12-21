import sys
#sys.stdin = open('input.txt','rt')

N = int(input())
for i in range(N):
    string = input().lower()
    cnt = 0
    for j in range(len(string)):
        if string[0+j] == string[-1-j]:
            cnt += 1
    if cnt == len(string):
        print('#{} YES'.format(i+1))
    else:
        print('#{} NO'.format(i+1))
