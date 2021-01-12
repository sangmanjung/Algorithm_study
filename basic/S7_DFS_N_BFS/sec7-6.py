#import sys
#sys.stdin = open('input.txt','rt')

def DFS(en,de): # en: encoding index, de = decoding index
    global cnt
    if en == nums:
        cnt += 1
        for j in range(de):
            print(chr(decoding[j]+64),end = '') # ASCII
        print()
    else:
        for i in range(1,27): # state-space tree 가지
            # 1자리수
            if encoding[en] == i:
                decoding[de] = i
                DFS(en+1,de+1)
            # 2자리수
            elif i >=10 and encoding[en] == i//10 and encoding[en+1] == i%10:
                
                '''
                조건1 : i가 2자리수인지 확인
                조건2 : 10 자리수의 값이 26을 넘어가지 않는지 확인
                조건3 : 1 자리수의 값이 26을 넘어가지 않도록 확인
                '''
                decoding[de] = i
                DFS(en+2,de+1) # 두자리수 저장이므로 한칸 더 앞으로

if __name__ == '__main__':
    encoding = list(map(int,input()))
    nums = len(encoding)
    encoding.insert(nums,-1) # list index error 방지용
    decoding = [0]*nums
    cnt = 0
    DFS(0,0)
    print(cnt)