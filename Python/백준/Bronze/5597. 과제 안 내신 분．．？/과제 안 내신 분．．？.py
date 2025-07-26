k=[]
a=[]
for i in range(28):
    b = int(input())
    a.append(b)
for i in range(1,31):
    if i not in a:
        k.append(i)
print(min(k))
print(max(k))