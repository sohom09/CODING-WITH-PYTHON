#To find the third largest/smallest number in a list
lst=eval(input("Enter a list of numbers:"))
lst.sort()
print("Sorted list=",lst)
l=len(lst)
print("3rd Largest number in the list=",lst[l-3])
print("3rd Smallest number in the list=",lst[2])
