def fact(no):
    if no==0:
        return 1
    else:
        return no*fact(no-1)
n=int(input("Enter the number: "))
print("The factorial is: ",fact(n))
