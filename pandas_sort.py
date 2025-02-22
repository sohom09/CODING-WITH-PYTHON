import pandas as pd
s11=pd.Series([6700, 5600, 5000, 5200], index=["A", "B", "C", "D"])
print("series object1 : ")
print(s11)
print(s11.sort_values())
print(s11.sort_index())
print(s11.sort_values(ascending=False))
