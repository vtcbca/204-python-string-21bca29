#WAS to enter any no and print from which no 0 to 9 it is divisible
n=int(input("Enter any number:"))
for i in range(1,9):
    if(n%i==0):
        print("{} is divisible by {}".format(n,i))
