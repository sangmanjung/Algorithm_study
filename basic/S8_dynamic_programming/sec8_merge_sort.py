# 병합 정렬 (merge sort)
'''
<순서>
1. 정렬하기 위한 리스트의 중앙값을 잡음 (mid = (left + right) // 2)
2. 절반으로 잘린 두 리스트를 각각 상태트리(이진트리)로 하여 시작 (후위순회)
3. 각각 잘린 두 리스트에 대한 정렬작업을 한 후 다시 리스트를 병합해야함
3-1. 재귀로 가지를 뻗고 다음 가지로 가기 전에 mid == 0 이면 종료
3-2. 재귀로 가지를 뻗을 때는 mid == 1 일 때 병합 조건: lt 와 rt 대소비교해서 tmp에 넣어주는 것으로 병합
3-3. 만약 두 가지에서 각각 2개짜리 리스트 두개가 나오면 tmp로 원래 행렬에 붙여넣어줌
4. 이러한 방식으로 재귀를 돌며 size = 1 단위의 리스트부터 병합해나가는 방법

==> 병합정렬은 리스트에 재귀와 이분탐색을 적용하여 가장 작은 리스트 단위부터 병합해나가며 정렬하는 방법
'''
def Dsort(lt,rt): # lt: 리스트의 맨 왼쪽, rt: 맨 오른쪽
    if lt < rt:
        mid = (lt+rt)//2
        ## (1) 가지 뻗기를 먼저 다 하고..
        Dsort(lt,mid)
        Dsort(mid+1,rt) # mid+1이 나머지 절반

        ## (2) 마지막까지 뻗은 가지에서 병합을 하는 과정
        p1,p2 = lt,mid+1 #절반의 왼쪽부분의 왼쪽 끝 / 오른쪽부분의 왼쪽 끝

        tmp = []
        while p1 <= mid and p2 <= rt: # 절반의 어느쪽이든 왼쪽부터 오른쪽까지 돌면
            if a[p1] < a[p2]: # 작은 것부터 tmp에 넣어주기 위함 
                tmp.append(a[p1]) 
                p1 += 1
            else:
                tmp.append(a[p2])
                p2 += 1

        if p1 <= mid: # 전부 들어가지 않은 원소들은 (그것이 p1이면)
            tmp = tmp + a[p1:mid+1] # tmp에 p1부터 남은 부분 마저 병합해서 넣어줌
        if p2 <= rt:
            tmp = tmp + a[p2:rt+1] # tmp에 p1부터 남은 부분 마저 병합해서 넣어줌

        for i in range(len(tmp)):
            a[lt+i] = tmp[i] # lt가 정렬 기준이므로..

if __name__ == '__main__':
    a = [23,11,45,36,15,67,33,21]
    print('Before sort: ',end = '')
    print(a)
    Dsort(0,7)
    print()
    print('After sort: ',end = '')
    print(a)
