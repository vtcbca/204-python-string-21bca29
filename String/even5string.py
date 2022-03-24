#write a script to enter 5 string in a list and check and print string whose length has even number of character without any string function.
def createlist():
    l=[]
    for i in range(5):
        a=input("Enter string:")
        l.append(a)
    return(l)
a=createlist()
for i in a:
    print(i)
    
