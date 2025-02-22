#Given the school result data, analyses the performance of the students
#on different parameters, e.g.- subject wise or class wise.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
subjects=['Physics', 'Accountancy', 'Mathematics', 'Computer', 'Home science']
percentage=[80,75,70,78,82]
#to draw line in red colour
plt.bar(subjects,percentage,align='center', color='green')
#to write the title of the line chart
plt.title('MARKS SCORED')
#to put label at X axis
plt.xlabel('Subjects')
#to put label at Y axis
plt.ylabel("MARKS PERCENTAGE")
plt.show()
