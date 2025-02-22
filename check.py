st=input("Enter a string: ")
a=0
e=0
p=0
t=0
u=0
for i in st:
    if i=='A' or i=='a':
        a=a+1
    if i=='E' or i=='e':
        e=e+1
    if i=='I' or i=='i':
        p=p+1
    if i=='O' or i=='o':
        t=t+1
    if i=='U' or i=='u':
        u=u+1
print("Frequency of A",a)
print("Frequency of E",e)
print("Frequency of I",p)
print("Frequency of O",t)
print("Frequency of U",u)



