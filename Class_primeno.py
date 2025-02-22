class primeno:
    def isprime(self,a):
        c=0
        if(a==0 or a==1):
            print("PRime nor composite")
        else:
            for i in range(2,a):
                if(a%i==0):
                    c=1
            if(c==0):
                print("this is a prime number")
            else:
                print("This is not a prime number")

        
t=primeno()
while(1):
    n=int(input("ENter a number: "))
    t.isprime(n)



