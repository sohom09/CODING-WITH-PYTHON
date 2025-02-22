h=int(input("ENTER HEIGHT: "))
for i in range(1,h+1,1):
    for s in range(i,h+1,1):
        print(" ", end="")
    for j in range(1,i+1,1):
        if(i%2!=0):
            print("*", end=" ")
    print()
for i in range(h-2,1-1,-1):
    for s in range(i,h+1,1):
        print(" ", end="")
    for j in range(1,i+1,1):
        if(i%2!=0):
            print("*", end=" ")
    print()
