lst=[]
n=int(input("Enter number of elements: "))
for i in range(0,n):
    ele=int(input( ))
    lst.append(ele)
print("original list:", lst)
print("elements with their frequency")
freq={}
for item in lst:
    if(item in freq):
        freq[item]+=1
    else:
        freq[item]=1
for key,value in freq.items():
    print("%d:%d"%(key,value))
