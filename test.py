# library 
import os
import pandas as pd
from sklearn.model_selection import train_test_split

# import
#print(os.getcwd())
#print(os.listdir())

path = "default of credit card clients.xlsx"
df = pd.read_excel(path, skiprows=1)

# vérif
print(df.head(5))
print(df.shape) 

df.info()
print(df.isna().sum().sum()) # => pas de valeurs manquantes
print(df.duplicated().sum()) # => pas de doublons

# nettoyage et mise en forme
df = df.rename(columns={"PAY_0" : "PAY_1",
                        "default payment next month" : "DEFAULT"})

print("Taux de défault :", df["DEFAULT"].mean().round(3))

for col in ["EDUCATION", "MARRIAGE"]:
    print(df[col].value_counts().sort_index(), "\n")
# => recodage des variables non documentés en autre
df["EDUCATION"] = df["EDUCATION"].replace({0: 4, 5: 4, 6: 4})
df["MARRIAGE"] = df["MARRIAGE"].replace({0: 3})

# => recodage status de remb non docu
# justification de mon choix : on s'intéresse au defaut donc ce qui compte c'est le retard,
# les valeurs -2 et 0 ne correspondent pas à un retard donc on les recode en -1 (pas de retard)
pay_cols = [f"PAY_{i}" for i in range(1, 7)]
df[pay_cols] = df[pay_cols].replace({-2: -1, 0: -1})
print(pd.Series(df[pay_cols].values.ravel()).value_counts().sort_index())


# découpage train / test 
SEED = 42
X = df.drop(columns="DEFAULT")
y = df["DEFAULT"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=SEED)
print("Taux de défaut train/test :", y_train.mean().round(3), y_test.mean().round(3))
