#WAS to enter any number and check number is armstrong or not
a=int(input("Enter any number:"))
no=a
sum=0
while(a>0):
    r=a%10
    sum=sum+r*r*r
    a=a//10
if(sum==no):
    print("{} Number is armstrong number".format(no))
else:
    print("{} Number is not a armstrong number".format(no))
