#print the words starting with a particular alphabet in a user entered string
st=input("Enter a sentence:")
new_st=""
word=""
letter=input("Enter a letter to merge with every words:")
lst=st.split()
for i in range (len(lst)):
    word=lst[i]
    new_st=new_st+letter+word+" "
print("After merging the alphabet with every word, the new sentence:",new_st)


