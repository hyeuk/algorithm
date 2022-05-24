
n,k = map(int,input().split())

cnt = 0

for i in range(100):
    
    if n%k == 0:
        n = n/k
        cnt+=1
        if n==1:
            break
    elif n%k > 0:
        n-=1
        cnt+=1
        if n==1:
            break

print(cnt)

