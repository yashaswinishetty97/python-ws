c = ['1','2','3']
f = ['1','3','5']
b = ['1','3','9']

lst = []

lst.extend(c)
lst.extend(f)
lst.extend(b)
newlst = []

for i in lst:
    if i in newlst:
        pass
    else:
        newlst.append(i)

print(newlst)