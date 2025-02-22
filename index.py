st=input("ENTER MAIN STRING: ")
fst=input("ENTER SUBSTRING: ")
for i in range(len(st)-len(fst)+1):
    sub=st[i:i+len(fst)]
    if(sub==fst):
        print(f"'{fst}' found at {i} index in '{st}' ")