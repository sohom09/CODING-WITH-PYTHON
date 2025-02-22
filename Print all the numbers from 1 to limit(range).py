#Input a limit and print all the numbers from1 to  that limit divided by 10
L=int(input("Please enter a limit : "))
for L in range(1,L+1):
    if(L%10==0):
        print(L)
