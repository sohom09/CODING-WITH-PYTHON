#importing and exporting data between pandas and CSV file

import pandas as pd
df=pd.read_csv("result.csv")
print("..... Importing Data from CSV FIle ")
print("************************Marksheet******************************")
print(df)

marks={"rollno":[11,35,26,17,25], "names":['arpan', 'rajorshi', 'robin', 'sourav', 'rakesh'],
       'english':[60,99,80,90,55], "maths":[84,68,77,75,72], 'IP':[71,99,91,48,43],
       "accounts":[63,95,74,84,76], 'bst':[54,68,67,38,37]}
result=pd.DataFrame(marks)
print("***********************Marksheet*********************")
print(result)
result.to_csv("NewResult.csv")
print("data has been exported to the csv file...")

#-----------------------the program ends here------------------------------
