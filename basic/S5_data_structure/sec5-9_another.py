import sys
#sys.stdin = open('input.txt','rt')

a1 = input()
a2 = input()

d1 = [0]*52 # A~Z(26) + a~z(26) = 52
d2 = [0]*52

## add 1 to each ascii index
for x in a1:
    if x.isupper(): # A~Z ?
        # ord(x) : ascii number
        # A~Z == 65~90, a~z == 97~122
        d1[ord(x)-65] += 1 # index: 0 ~ 25
    else:
        d1[ord(x)-71] += 1 # index: 26 ~ end

for x in a2:
    if x.isupper(): # A~Z ?
        # ord(x) : ascii number
        # A~Z == 65~90, a~z == 97~122
        d2[ord(x)-65] += 1 # index: 0 ~ 25
    else:
        d2[ord(x)-71] += 1 # index: 26 ~ end

for i in range(52):
    if d1[i] != d2[i]:
        print('NO')
        break
    else:
        print('YES')
