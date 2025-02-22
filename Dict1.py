n=int(input("Enter the number of students you want to access : "))
st={}
stud={}
for i in range(1,n+1):
    n=input("enter the name : ")
    st["name"]=n
    a=input("enter the address : ")
    st["add"]=a
    p=input("enter the phn no : ")
    st["ph"]=p
    stud[i]=st
    st={}
print("Name\tAddress\tPhn no")
for i in range(1,n+1):
    print(stud[i]["name"],end="\t")
    print(stud[i]["add"],end="\t")
    print(stud[i]["ph"],end="\t")
    
    
