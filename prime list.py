list=[]
c=0
for i in range(1,11):
    a=int(input("Enter the no of elements: "))
    list.append(a)
for i in list:
    for j in range(1,i+1):
        if (i%j==0):
            c=c+1
    if(c==2):
      print(i)
    c=0
