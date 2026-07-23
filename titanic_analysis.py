import pandas as pd

#Loading the dataset
df = pd.read_csv("titanic.csv")

#Explore the dataset
print(df.head())
print(df.shape)
print(df.info())

#Overall survival rate
print(df["Survived"].mean())

#Survival rate by gender
print(df.groupby("Sex")["Survived"].mean())

#Survival rate by class
print(df.groupby("Pclass")["Survived"].mean())

#Average age: survivors vs non-survivers
print(df.groupby("Survived")["Age"].mean())