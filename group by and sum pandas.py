#python program to create a pandas dataframe qtr sales and print group by func by rows and print total exp
#importing pandas and numpy modules
import pandas as pd
import numpy as np
qtr_sales=pd.DataFrame({'Item category':['A','B','C','B','A','C','C','A','B'],
                        'Item Name':['Ipad','Laptop','Fridge','Cooler','Iwatch','AC','Hard Disk','IPendrive','Smartboard'],
                        'Expenditure':[28800,43600,34600,7500,56000,46000,16000,14236,65980]
                        })
print(qtr_sales)
#grouping the rows and priting the total expenditure per category
print("Total expenditure per category is :")
print(qtr_sales.groupby('Item category')['Expenditure'].sum())
