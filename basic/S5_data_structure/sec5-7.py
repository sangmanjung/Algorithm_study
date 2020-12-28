import sys
from collections import deque
#sys.stdin = open('input.txt','rt')

sub_original = input()
N = int(input())

for i in range(N):
    result = True
    plan = list(map(str,input()))
    sub_new = deque(list(map(str,sub_original)))

    for x in plan:
        if x == sub_new[0]:
            sub_new.append(sub_new.popleft())
        elif x == sub_new[0] and x == sub_new[-1]:
            continue
        else:
            if x in list(sub_new):
                result = False
                break
            else:
                continue

    sub_new = ''.join(map(str,sub_new))

    if result == False:
        print('#%d NO' % (i+1))
    else:
        if sub_original == sub_new:
            print('#%d YES' % (i+1))
        else:
            print('#%d NO' % (i+1))

    
            