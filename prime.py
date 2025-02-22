n=int(input("Enter a number: "))
c=0
for i in range(1,n+1):
    if(n%i==0):
        c+=1
if(c==2):
    print("PRIME")
else:
    print("NOT")
l=int(input("ENTER THE LOWER BOUNDARY OF THE RANGE: "))
u=int(input("ENTER THE UPPER BOUNDARY OF THE RANGE: "))