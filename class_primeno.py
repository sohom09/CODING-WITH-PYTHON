class pr:
    def isprime(self,n):
        c=0
        for i in range(1,n+1):
            if(n%i==0):
                c+=1
        if(c==2):
            print("PRIME")
        else:
            print("NOT PRIME")
a=pr()
x=int(input("ENTER THE NUMBER: "))
a.isprime(x)
        
