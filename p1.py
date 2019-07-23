import random as rn

num=rn.randint(1,7)
count=0
while True:
   inp=int(input("enter a number"))
   if inp==num:
      count+=1
      print(f"you guessed number in (count) attempts")
      break
   elif inp< num:
      print("less than")
      count+=1
      
   else:
      print("more than")
      count+=1
      
   if count==3:
      print("better luck next time")
      break