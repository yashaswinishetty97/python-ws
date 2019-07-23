data = input("Enter the list of element ")
names = data.upper().split(",")
newlst = []

for i in names:
    if i.startswith("A") or i.endswith("H"):
        newlst.append(i)

newlst.sort()

print(newlst)



