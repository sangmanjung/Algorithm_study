# 퀵 정렬 (quick sort)
'''
<순서>
1. 정렬하기 위한 리스트의 pivot 값을 잡음.(병합정렬은 중앙값이지만 퀵은 pivot 방법 다양함)
1-1. pivot은 보통 리스트 맨 오른쪽 끝으로 잡음 (pivot = a[-1])
2. pivot을 기준으로 pivot과 대소비교 함 (전위순회)
2-1 맨 왼쪽 끝을 pos로 두고 그 다음 값부터 pivot과 대소비교
2-2 그 다음값이 pivot 보다 작으면 pos와 그 다음값과 자리바꿈
2-3 pos를 그 다음값으로 정하고 pos의 다음값과 마찬가지로 비교 반복
3. pivot이 자기자신보다 작은값과 큰값 사이에 위치하게 됨
4. 이제 작은값과 큰값 두개 리스트에 대한 전위순회 재귀로 들어감
5. 재귀 반복을 마치게 되면 자동으로 리스트가 정렬되게 됨.

==> 리스트 맨 오른쪽 값과 맨 왼쪽값을 각각 pivot, pos로 잡고
pos 다음지점부터 loop를 돌면서 pivot보다 작은 값은 스와프하고 재귀 들어가는 방식
'''
def Qsort(lt,rt):
    if lt < rt:
        pos = lt # 분할된 영역의 시작지점이어야 하므로 lt로 지정
        pivot = a[rt] # 분할된 영역의 끝지점이어야 하므로 rt로 지정
        for i in range(lt,rt): # 재귀 전 pivot 위치 잡기
            if a[i] <= pivot: # swap를 위한 조건
                a[i],a[pos] = a[pos],a[i]
                pos += 1
        a[rt],a[pos] = a[pos],a[rt] # 마지막 값인 pivot과 pos 자리마꿈으로써 분할 마침
        Qsort(lt,pos-1) # pivot 기준으로 작은값 재귀
        Qsort(pos+1,rt) # pivot 기준으로 큰값 재귀

if __name__ == '__main__':
    a = [45,21,23,36,15,67,11,60,20,33]
    print('Before sort: ',end = '')
    print(a)
    Qsort(0,9)
    print()
    print('After sort: ',end = '')
    print(a)
