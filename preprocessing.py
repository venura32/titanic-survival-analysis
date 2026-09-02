import pandas as pd

df = pd.read_csv("titanic.csv")

# Check missing values 
print(df.isnull().sum())

# Drop the Cabin column
df = df.drop(columns=["Cabin"])

# Fill missing Age with the average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Drop rows where Embarked is missing
df = df.dropna(subset=["Embarked"])

# Confirm no missing values remain
print(df.isnull().sum())


import matplotlib.pyplot as plt

#Use yopur actual file path
df = pd.read_csv('titanic.csv')
plt.hist(df['Age'])
plt.show()

plt.hist(df['Fare'])
plt.show()

#To do the side by side comparison of Fare/Pclass using boxplot
df.boxplot(column='Fare' , by='Pclass')
plt.show()

df.boxplot(column='Fare' , by='Embarked')
plt.show()
