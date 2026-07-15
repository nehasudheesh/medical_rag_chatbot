import pandas as pd

# Load datasets
description_df = pd.read_csv("data/symptom_Description.csv")
precaution_df = pd.read_csv("data/symptom_precaution.csv")

# Merge datasets
knowledge_base = pd.merge(
    description_df,
    precaution_df,
    on="Disease",
    how="inner"
)

# Replace missing values
knowledge_base.fillna("Not Available", inplace=True)

# Create a single text column
knowledge_base["Knowledge"] = (
    "Disease: " + knowledge_base["Disease"] +
    ". Description: " + knowledge_base["Description"] +
    ". Precautions: " +
    knowledge_base["Precaution_1"] + ", " +
    knowledge_base["Precaution_2"] + ", " +
    knowledge_base["Precaution_3"] + ", " +
    knowledge_base["Precaution_4"]
)

# Save the processed knowledge base
knowledge_base.to_csv(
    "data/medical_knowledge_base.csv",
    index=False
)

print("Knowledge base created successfully!\n")

print(knowledge_base[["Disease", "Knowledge"]].head())