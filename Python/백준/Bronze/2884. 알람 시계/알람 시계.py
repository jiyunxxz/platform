h,m = map(int,input().split())

if m-45>=0:
    k = f"{h} {m-45}"
    print(k)
elif m-45<0:
    m1 = 60-(45-m)
    if h==0:
        print(23,m1)
    else:
        print(h-1,m1)