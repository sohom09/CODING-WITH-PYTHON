import pandas as pd
from sqlalchemy import create_engine
import pymysql
engine=create_engine(host= "localhost", user = "root", passwd= "ApSc1233@#", database= "student")
if mycon.is_connected():
    print("successfully connected to MySQL Database")
    df1=pd.read_sql("select * from employee where empID=3", mycon)
    print(df1)
