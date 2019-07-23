'''program to check whether a given number is palindrome'''
n=int(input("enter the number:")
rev=0
temp=n
while temp>0:
   rev=rev*10+(temp%10)
   temp=temp//10
if rev==n:
   print("it is a palindrome")
else:
   print("it is not a palindrome")