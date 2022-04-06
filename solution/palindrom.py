#WAS to enter any number and check number is palindrome or not
a=int(input("Enter any number:"))
no=a
sum=0
while(a>0):
    r=a%10
    sum=sum*10+r
    a=a//10
if(sum==no):
    print("{} is a palindrom number".format(no))
else:
    print("{} is not a palindrom number".format(no))
