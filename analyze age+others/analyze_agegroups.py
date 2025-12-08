import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Hospital_data_completed.csv")

# Define age groups
def age_group(age):
    if age < 40:
        return "30-39"
    elif age < 50:
        return "40-49"
    elif age < 60:
        return "50-59"
    else:
        return "60+"

df["Age_Group"] = df["Age"].apply(age_group)

# Basic analysis
print("Patient count by age group:")
print(df["Age_Group"].value_counts())

print("\nAverage spending by age group:")
print(df.groupby("Age_Group")["Total_Spending"].mean())

print("\nAverage annual visits by age group:")
print(df.groupby("Age_Group")["Annual_Visits"].mean())

print("\nInsurance type distribution by age group:")
print(df.groupby(["Age_Group", "Insurance_Type"]).size())

# Visualization
plt.figure(figsize=(12,6))

# Bar chart: patient count by age group
plt.subplot(1,2,1)
df["Age_Group"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Patient Count by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Count")

plt.show()