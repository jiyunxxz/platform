c=[]
k=[]
ch1 = 0
for i in range(10):
    a = int(input())
    b = a%42 
    c.append(b)
for i in range(43):
    if c.count(i) !=0:
        k.append(i)
print(len(k))