#to search for an element which index number
list1=list()
sum=0
num=int(input("Enter the size of the list :"))
print("Enter the number: ")
for a in range(int(num)):
    l=int(input(""))
    list1.append(int(l))
    print("Entered list: ",list1)
    x=int(input("Enter number to be searched: "))
    found=False
    for i in range(len(list1)):
        if(list[i]==x):
            found=True
        print("% found at %dth position"%(x,i))
        break
if(found==False):
        print("%d is not in list",x)
