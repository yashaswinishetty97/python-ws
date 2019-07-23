import random as rn
lst = []
for i in range (1,101):
    lst.append(rn.randint(1,1000))
print(lst)  
new_lst = []
for i in lst:
    if i % 3 == 0 and i % 6 ==0 and \
       not i % 9 == 0:
       new_lst.append(i)
print(new_lst)