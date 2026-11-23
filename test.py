# library 
import os
import pandas as pd

# import
print(os.getcwd())
print(os.listdir())

path = "default of credit card clients.xlsx"
df = pd.read_excel(path, skiprows=1)

# stat desc
print(df.head(5))
print(df.shape) 

