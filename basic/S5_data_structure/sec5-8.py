import sys
#sys.stdin = open('input.txt','rt')

# Hash is the data structure using 'dictionary' in python
N = int(input())
H = dict()

for i in range(N):
    H[input()] = 1 # generate dictionary[key] = value

for i in range(N-1):
    H[input()] = 0 # check

for k, v in H.items():
    if v == 1:
        print(k)
        break

'''
## if not use 'Hash', then 

notes = [input() for _ in range(N)]
poem = [input() for _ in range(N-1)]

for i in range(N):
    for j in range(N-1):
        if notes[i] == poem[j]:
            notes[i] = 1

for i in range(N):
    if notes[i] != 1:
        print(notes[i])
'''
