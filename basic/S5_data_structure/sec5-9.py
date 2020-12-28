import sys
#sys.stdin = open('input.txt','rt')

a1 = input()
a2 = input()
d1 = dict()
d2 = dict()

for x in a1:
    # dict.get(key,if not in -> return 0)
    d1[x] = d1.get(x,0) + 1

for x in a2:
    d2[x] = d2.get(x,0) + 1
    
'''
## NOTE)

it is possible that

for x in a1:
    d[x] = d.get(x,0) + 1

for x in a2:
    d[x] = d.get(x,0) - 1

for x in a1:
    if d.get(x) > 0:
        print('NO')
        break
else:
    print('YES')
'''

for i in d1.keys():
    if i in d2.keys(): # is it in d2?
        if d1[i] != d2[i]: # compare counts
            print('NO')
            break
    else:
        print('NO')
        break
else:
    print('YES')
