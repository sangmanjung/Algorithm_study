import sys
#sys.stdin = open('input.txt','rt')

B = input()
stack = []

cnt = 0
for i in range(len(B)):
    if B[i] == '(':
        stack.append(B[i])
    else:
        stack.pop() # () or (( )<- closed
        if B[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)

