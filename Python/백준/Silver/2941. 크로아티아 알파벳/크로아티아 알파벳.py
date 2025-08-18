a = input()

cr = ['dz=','c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cr:
    a = a.replace(i,"1")

print(len(a))