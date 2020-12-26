import sys
#sys.stdin = open('input.txt','rt')

N = int(input())
L = list(map(int,input().split()))

left = 0
right = N-1
last = 0
inc = []
result = ''
while left <= right:
    # take both
    if L[left] > last:
        inc.append((L[left],'L'))
    if L[right] > last:
        inc.append((L[right],'R'))

    inc.sort() # for the criterion 'if inc[0][1]' later

    if len(inc) == 0:
        break
    else:
        result = result + inc[0][1]
        last = inc[0][0] # save the last selection
        if inc[0][1] == 'L':
            left += 1
        else:
            right -= 1

    inc.clear() # reset the current results

print(len(result))
print(result)
