## section 5 1~3 (stack problems) need to resolve
import sys
#sys.stdin = open('input.txt','rt')

f = input()
f = list(map(str,f))

stack = []
result = ''
for x in f:
    if x.isdecimal():
        result += x
    else: 
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

while stack:
    result += stack.pop()

print(result)
