import sys
#sys.stdin = open('input.txt','rt')

s = input()

n = []
for i in s:
    if i.isdigit():
        n.append(i)

'''
# another method
(string convert to number without 0)
num = 0
for i in s:
    if i.isdigit():
        num = num*10 + int(i)
'''

num = ''
for j in n:
    num += j
num = int(num)
print(num)

cnt = 0
for k in range(1,num+1):
    if num % k == 0:
        cnt += 1
print(cnt)