n = int(input())
a = list(map(int,input().split()))
max = max(a)
l=[]
sum=0
for i in range(n):
    new = a[i-1]/max*100
    l.append(new)
for i in range(n):
    sum += l[i-1]
print(sum/n)