#for the data frames created above analyze and plot appropriate charts with title and legend.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
df=pd.read_csv("Student_result.csv")
plt.hist([df['ENG'],df['BENG'],df['MATHS'],df['SCIENCE'],df['SSC'],df['PED'],df['CA']],
         color=['red', 'yellow', 'blue', 'green', 'orange', 'black', 'pink'])
plt.title('number of Students against scores')
plt.xlabel('score')
plt.ylabel('Number of students')
plt.legend(['Eng', 'Hindi', 'Maths', 'Science', 'S.Sc', 'Phy Edu', 'CA'])
plt.show()
