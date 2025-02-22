words='welcome to the world of programming'.split()
msg=[[word.upper(),word.lower(),len(word)] for word in words]
for i in msg:
    print(i)
