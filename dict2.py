#Create a dictionary to store names of states and their capitals
n=int(input("Enter how many elements you want to work with the dictionery:"))
dict={}
for i in range(n):
    state=input("enter a state:")
    capital=input("enter the corresponding capital:")
    dict[state]=capital
print("dicionery with the state and their capitals are:",dict)
