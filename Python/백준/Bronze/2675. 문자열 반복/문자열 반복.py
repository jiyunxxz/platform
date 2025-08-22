a =int(input())
for i in range(a):
    b= input().split()
    k = b[1]
    c=[]
    for ch in k:
        ny = ch*int(b[0])
        c.append(ny)
    print(''.join(c))