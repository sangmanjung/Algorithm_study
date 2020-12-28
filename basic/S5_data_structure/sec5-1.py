import sys
#sys.stdin = open('input.txt','rt')

nums,m = map(int,input().split())
nums = list(map(int,str(nums)))

stack = []

for x in nums: # choose the element
    # compare each element in stack
    while stack and m > 0 and stack[-1] < x: 
        stack.pop() # delete
        m -= 1
    # if stack = [], then insert the first element in nums
    stack.append(x)
if m != 0:
    stack = stack[:-m] # 0 ~ end-2 (== -3)

print(''.join(map(str,stack)))