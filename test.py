# library 
import os
import pandas as pd
import sklearn

# import
#print(os.getcwd())
#print(os.listdir())

path = "default of credit card clients.xlsx"
df = pd.read_excel(path, skiprows=1)

# vérif
print(df.head(5))
print(df.shape) 

# nettoyage et mise en forme
df = df.rename(columns={"PAY_0" : "PAY_1",
                        "default payment next month" : "DEFAULT"})

print("Taux de défault :", df["DEFAULT"].mean().round(3))

for col in ["EDUCATION", "MARRIAGE"]:
    print(df[col].value_counts().sort_index(), "\n")
# => recodage des variables non documentés en autre
df["EDUCATION"] = df["EDUCATION"].replace({0: 4, 5: 4, 6: 4})
df["MARRIAGE"] = df["MARRIAGE"].replace({0: 3})
