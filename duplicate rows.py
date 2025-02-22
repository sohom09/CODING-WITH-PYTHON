# program to filter out rows based on different criteria such as duplicate rows
import pandas as pd
data={'Name':['Aman', 'Rohit', 'Deepika', 'Aman', 'Deepika', 'Sohit', 'Geeta'],
      'Sales':[8500,4500,9200,8500,9200,9600,8400]}
sales=pd.DataFrame(data)
print(sales)
#find duplicate rows
duplicated=sales[sales.duplicated(keep=False)]
print("duplicate Row: \n",duplicated)

#-----------------------------thr program ends here--------------------------
