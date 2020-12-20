N,K = map(int,input().split())
card = list(map(int,input().split()))

record = set()
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            record.add(card[i]+card[j]+card[k])

result = sorted(list(record), reverse = True)

print(result[K-1])
