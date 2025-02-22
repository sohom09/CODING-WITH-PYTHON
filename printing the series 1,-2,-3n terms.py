#Print the series: 1, -2, 3, -4....N (N should input)
n=int(input("Enter the limit="))
for i in range(1,n+1):
    if(i%2!=0):
        print(i,end=",")
    if(i%2==0):
        print(-i,end=",")

