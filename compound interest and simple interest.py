#python program to find out the simple interest and compound interest
p=float(input("Enter the principle amount:"))
r=float(input("Enter the rate in percentage:"))
t=float(input("Enter the time in years:"))
#Enter the no of frequency as: 1-yearly,2-Half yearly,4-quaterly and 12-monthly
n=float(input("Enter the frequency of compound interest:"))
#calculating the si and ci by applyting formula
si=(p*r*t)/100
a=p*(1+(r/100)/n)**(n*t)
#printing the compound interest and simple interest
print("Simple interest : " ,si)
print("Compound interest : " ,a-p)
