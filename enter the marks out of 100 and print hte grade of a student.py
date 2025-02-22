#Python program to enter a marks out of 100 and print the grade
m=float(input("Enter a marks out of 100 :"))
if m>=80.5 and m<=100:
    print("Your grade is A")
elif m>=60.5 and m<80.5:
    print("Your grade is B")
elif m>=40.5 and m<60.5:
    print("Your grade is C")
elif m>=20.5 and m<40.5:
    print("Your grade is D")
elif m>=0 and m<20.5:
    print("Your grade is E")
else:
    print("Enter a Valid marks out of 100")
