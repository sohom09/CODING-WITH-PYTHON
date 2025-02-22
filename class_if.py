class ifi:
    def calculate(self,a,b):
        sum=a+b
        p=a*b
        if(a>b):
            return(sum)
        else:
            return(p)

t=ifi()
z=t.calculate(3,5)
print(int(z))
