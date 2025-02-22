list=[]
s=0
for i in range(1,21):
    a=int(input("Enter the number of elements: "))
    list.append(a)
for i in list:
    for j in range(1,i):
        if(i%j==0):
            s=s+j
    if(s==i):
        print(i)
    s=0
    
