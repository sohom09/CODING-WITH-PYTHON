#Find the compound interest by taking principal, rate, time and compound frequency as input.
p=float(input("enter the principle amount:"))
r=float(input("enter the rate in percentage:"))
t=float(input("enter the time in years:"))
n=float(input("enter the n no. of frequency:"))
ci=p*((n*100+r)/(n*100))**(n*t)
print("compound interest=",ci)

