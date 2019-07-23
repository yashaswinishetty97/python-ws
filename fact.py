num = int(input("enter the number"))
fact = 1
if num > 0:
   for i in range(num,1,-1):  
     fact = fact * i
print(f"factorial = {fact}")