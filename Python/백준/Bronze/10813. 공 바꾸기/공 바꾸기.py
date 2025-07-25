d=[]
n,m = map(int,input().split())
for i in range(n):
    d.append(i+1)
for i in range(m):
    i,j = map(int,input().split())
    i1 = d[i-1]  #리스트에서 값의 값을 찾고 싶을때는 리스트[위치]
    i2 = d[j-1]  #리스트에서 위치를 찾을 찾고 싶을때는 리스트.index[값]
    d[i-1] = i2
    d[j-1] = i1
print(*d)