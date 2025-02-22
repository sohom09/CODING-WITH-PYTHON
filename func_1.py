s=0
p=0
def calculate(a,b):
    if(a>b):
        s=a+b
    else:
        s=a*b
    return(s)

n1=int(input("Enter first number: "))
n2=int(input("Enter 2nd number: "))
p=calculate(n1,n2)
print(p)
