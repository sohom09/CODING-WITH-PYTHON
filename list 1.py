#to count the frequency of elements in a list
a=[]
n=int(input("Enter number of elements: "))
for i in range(1,n+1):
    b=int(input("Enter element: "))
    a.append(b)
K=0
num=int(input("Enter the number to be counted: "))
for j in a:
    if(j==num):
        K=K+1
print("Number", num, " is apper", K, "times")
