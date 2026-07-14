import pandas as pd

description_df = pd.read_csv("data/symptom_Description.csv")
precaution_df = pd.read_csv("data/symptom_precaution.csv")

print("===== Disease Description Dataset =====")
print(description_df.info())

print("\n")

print("===== Precaution Dataset =====")
print(precaution_df.info())

print("\n")

print("Missing values in Description Dataset")
print(description_df.isnull().sum())

print("\n")

print("Missing values in Precaution Dataset")
print(precaution_df.isnull().sum())