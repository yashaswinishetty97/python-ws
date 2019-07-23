#program to calculate electricity bill
units=float(input("enter the no of units used"))
if(units<500 and units>=1):
  price=units*6
elif(units<1000 and units>=501):
  price=units*8
else:
  price=units*12
if(price<50):
  price=50
print(f"price={price}")
