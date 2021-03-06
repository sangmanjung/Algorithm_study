#import sys
#sys.stdin = open('input.txt','rt')

'''
문제 접근 -> DFS 문제인가? (yes) -> state-space tree 우선적으로 짤 것
state-space tree : 이진트리? 가짓수? 레벨은? =>> 결정
'''

def DFS(level,A,B,C):
    global result
    if level == coin:
        if A != B and A != C and B != C:
            difference = max(A,B,C) - min(A,B,C)
            if difference <= result:
                result = difference
    else:
        DFS(level+1,A + price[level],B,C)
        DFS(level+1,A,B + price[level],C)
        DFS(level+1,A,B,C + price[level])

if __name__ == '__main__':
    coin = int(input())
    price = [int(input()) for _ in range(coin)]

    result = 2147000000
    DFS(0,0,0,0)
    print(result)
