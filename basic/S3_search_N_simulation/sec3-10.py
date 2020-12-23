import sys
#sys.stdin = open('input.txt','rt')

L = [list(map(int,input().split())) for _ in range(9)]

st1 = st2 = 0
en1 = en2 = 3
iters = 0
while True:
    s = 1
    for i in range(st1, en1):
        for j in range(st2, en2):
            s *= L[i][j]
    if s == 362880:
        if iters == 8:
            print('YES')
            break
        else:
            if en2 == 9:
                st2,en2 = 0,3
                st1 += 3
                en1 += 3
            elif en2 < 9:
                st2 += 3
                en2 += 3
    else:
        print('NO')
        break
    iters += 1
