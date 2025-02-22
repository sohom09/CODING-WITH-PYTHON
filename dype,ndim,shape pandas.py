#python program to Create a dataframe for examination result and display row labels, column labels data types of each column and the dimension
import pandas as pd
import numpy as np
marks={'English':[40,38,36,45],
       'IP':[32,56,58,47],
       'Bst':[50,48,26,55],
       'Acct':[60,18,38,65],
       'total marks':[485,360,256,125], 'percentage':[60.5,89.5,76.5,80]
       }
result=pd.DataFrame(marks, index=['Sayan', 'Shuvamita', 'Sohom', 'Khalida'])
print(result)
print(result.columns)
print(result.index)
print(result.dtypes)
print(result.ndim)
print(result.shape)
