#To find the largest and smallest numbers in a list
lst=eval(input("Enter a list of numbers:"))
max=lst[0]
min=lst[0]
for i in range(len(lst)):
    if lst[i]>max:
        max=lst[i]
    if lst[i]<min:
        min=lst[i]
print("Largest number in the list=",max)
print("Smallest number in the list=",min)
