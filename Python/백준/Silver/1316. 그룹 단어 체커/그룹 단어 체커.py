a = int(input())
count =0

for i in range(a):
    word = input()
    b = set()
    c= ''
    g = True
    for ch in word:
        if ch != c:
            if ch in b:
                g = False
                break
            b.add(ch)
            c = ch
    if g:
     count+=1
print(count)