import sys
#sys.stdin = open('input.txt','rt')

N = int(input())
nums = list(map(str,input().split()))

def reverse(nums):
    revlist = []
    new_n = str()
    for i in range(len(nums)):
        tmp = list(range(len(nums[i]),0,-1))
        for j in range(len(tmp)):
            new_n += nums[i][tmp[j]-1]
        revlist.append(int(new_n))
        new_n = str()
    return revlist

def isPrime(revlist):
    M = max(revlist)
    check = [0]*(M+1)
    primelist = []
    for i in range(2,M+1):
        if check[i] == 0:
            primelist.append(i) 
            for j in range(i,M+1,i):
                check[j] = 1
    result = []
    for r in revlist:
        for p in primelist:
            if r == p:
                result.append(r)
    return result

revlist = reverse(nums)
reversed_prime = isPrime(revlist)

for i in range(len(reversed_prime)):
    print(reversed_prime[i],end = ' ')

