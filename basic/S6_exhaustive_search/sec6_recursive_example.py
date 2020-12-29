import sys
sys.stdin = open('input.txt','rt')

def DFS(x):
    if x > 0:
        '''
        print(x,end = ' ')
        DFS(x-1)

        answer : 3 2 1

        DFS(x-1)
        print(x,end = ' ')

        answer : 1 2 3

        reason why:
        재귀함수가 실행될때 내부에 있는 stack에
        stack frame 형태로 재귀함수에 대한 정보가 쌓이고
        최종적으로 실행되는 line의 코드로 복귀함.
        이 때, stack frame이 복귀하는 과정은
        stack 이기 때문에 후입선출의 방법을 따름.
        그래서 재귀함수를 먼저 호출하게 되면
        x = 0이 될때까지 함수를 호출하여 stack에 저장하고,
        이후 다음 line 코드를 실행할때는 반대의 순서로 출력이 됨 
        '''
        
        DFS(x-1)
        print(x,end = ' ')

if __name__ == '__main__':
    n = int(input())
    DFS(n)
