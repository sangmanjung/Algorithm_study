import sys
#sys.stdin = open('input.txt','rt')

N,M = map(int,input().split())
songs = list(map(int,input().split()))

left = 1
right = sum(songs)
result = 0

while left <= right:
    s = 0
    cnt = 1 # since we just slice twice times in the list if M = 3.
    middle = (left + right)//2

    for n in songs:
        if s+n > middle: # pre-test (capacity)
            cnt += 1
            s = n # now = the next song
        else:
            s += n

    if middle >= max(songs) and cnt <= M:
        '''
        counterexample:
        (reason for middle >= max(songs))
        input:
        9 9
        1 2 3 4 5 6 7 8 9
        '''
        result = middle
        right = middle - 1
    else:
        left = middle + 1

print(result)