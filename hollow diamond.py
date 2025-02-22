n=int(input("ENTER THE NUMEBR OF ROWS: "))
for i in range(1,n+1):
    for s in range(i,n):
        print(" ",end="")
    for j in range(1,i+1):
        if(j==1 or j==i):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
for i in range(n-1,1-1,-1):
    for s in range(i,n):
        print(" ",end="")
    for j in range(1,i+1):
        if(j==1 or j==i):
            print("* ",end="")
        else:
            print("  ",end="")
    print()