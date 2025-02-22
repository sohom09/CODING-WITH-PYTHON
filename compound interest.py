#to find the compound interest 
p=float(input("enter the principle amount:"))
r=float(input("enter the rate in percentage:"))
t=float(input("enter the time in years:"))
#Enter the no of frequency as: 1-yearly,2-Half yearly,4-quaterly and 12-monthly
n=float(input("enter the frequency of compound interest:"))
a=p*(1+(r/100)/n)**(n*t)
print("compound interest= ",a-p)

