a=[]
n,m = map(int,input().split())
for i in range(1,n+1):
    a.append(i)
for u in range(m):
    i,j = map(int,input().split())
    a[i-1:j] = a[i-1:j][::-1]
print(*a)