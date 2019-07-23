amt=float(input("enter the amount"))
if(amt>=10000):
   discount=amt*0.2
else:
   discount=amt*0.05
amount=amt-discount
print(f"amt={amt},discount={discount},amount={amount}")
