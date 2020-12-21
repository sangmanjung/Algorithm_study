import sys
sys.stdin = open('input.txt','rt')

N = int(input())
for i in range(N):
    string = input().lower()
    for j in range(len(string)//2):
        # alternative condition: s == s[::-1]
        if string[j] != string[-1-j]:
            print('#%d NO' % (i+1))
            break
    else:
        print('#%d YES' % (i+1))