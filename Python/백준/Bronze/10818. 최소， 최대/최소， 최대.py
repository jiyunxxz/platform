a = int(input())
b = list(map(int,input().split()))
d = []
max = max(b)
min = min(b)
d.append(min)
d.append(max)
print(*d)