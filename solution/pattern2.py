#WAS to enter any number to print  pattern
n=int(input("Enter any number:"))
for i in range(n):
    for j in range(i+1):
        print('',end='')
    for j in range(i,n):
        print("*",end='')
    print()
