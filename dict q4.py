dic={"nitin":(21,'NIIT'),"Ankit": (15,"NIIT")}
print("The original dictionary: " +str(dic))
result=[(key,i,j) for key,(i,j) in dic.items()]
print("The list after conversion:"+ str(result))
