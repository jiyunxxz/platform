hour,min = map(int,input().split())
time = int(input()) 

ans = time+min
if ans<60:
    print(hour,ans)
elif hour==23 and ans>=60:
    print((0+ans//60)-1,ans%60)
elif (hour+ans//60)>=24:
        print((hour+ans//60)-24,ans%60)
else:
    print(hour+ans//60,ans%60)