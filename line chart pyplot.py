#creating a line chart
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
games=["cricket", "badminton", "football", "volleyball", "tennis"]
india=[80,100,60,70,20]
australia=[90,70,60,50,40]
#plt.bar(games,india, width=[0.5,0.4,0.5,0.3,0.7], color=['b', 'c', 'k', 'r', 'b'])
plt.hist(games,australia,  oreintation='horizontal', cummulative='true')
plt.xlabel("sports")
plt.ylabel("scores")
plt.title("a line chart and a bar chart")
plt.figure(figsize=(15,7))
plt.show()
