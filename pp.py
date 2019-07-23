def is_prime(N)
   if N<2:
     return False
   for i in range(2,N//2+1):
     if N%i == 0;
       return False
   return True

N=int(input("enter the value for N"))
i=2
count=0
while True:
  if is_prime(I):
     print(i)
     count+=1
  i+=1
if count==N:
   break