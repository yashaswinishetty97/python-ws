#program to calculate tax
salary=float(input("enter the salary"))
if(salary<500000 and salary>=0):
  income=salary
elif(salary<1000000 and salary>=500001):
  income=salary-(salary*0.05)
else:
  income=salary-(salary*0.3)
print(f"sal={income}")
