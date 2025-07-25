d=[]
n,m = map(int,input().split())
for i in range(n):
    d.append(0)
for i in range(m):
    i,j,k = (map(int,input().split()))
    for i in range(i,j+1):
        d[i-1]=k
print(*d)