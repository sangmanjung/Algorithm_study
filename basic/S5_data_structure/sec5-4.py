import sys
#sys.stdin = open('input.txt','rt')

f = list(map(str,input()))

stack = []
for x in f:
    if x.isdecimal():
        stack.append(int(x))
    else:
        a = stack.pop()
        b = stack.pop()
        if x == '+':
            stack.append(a+b)
        elif x == '-':
            stack.append(b-a)
        elif x == '*':
            stack.append(a*b)
        elif x == '/':
            stack.append(b/a)

print(stack[0])