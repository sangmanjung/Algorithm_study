import sys
#sys.stdin = open('input.txt','rt')

N = int(input())
numbers = list(map(str,input().split()))

def digit_sum(numbers):
    sumlist = []
    for num in numbers:
        s = 0
        for n in num:
            s += int(n)
        sumlist.append(s)
    return sumlist

sumlist = digit_sum(numbers)
print(numbers[sumlist.index(max(sumlist))])


