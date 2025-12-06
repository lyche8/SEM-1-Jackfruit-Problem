import pandas as pd
import re
from collections import defaultdict

# ----------------------------------------
# 1) Load dataset
# ----------------------------------------
df = pd.read_csv("symtoms_df.csv")

# Drop unused column
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# ----------------------------------------
# 2) Clean & normalize symptoms
# ----------------------------------------
def clean_symptom(s):
    if pd.isna(s): 
        return None
    s = s.lower().strip()
    s = re.sub(r'[^a-z0-9\s_]', '', s)
    s = s.replace('_', ' ')
    s = re.sub(r'\s+', ' ', s)
    return s

# Apply cleaning
for col in ['Symptom_1','Symptom_2','Symptom_3','Symptom_4']:
    df[col] = df[col].apply(clean_symptom)

# ----------------------------------------
# 3) Build disease → symptoms dictionary
# ----------------------------------------
disease_symptoms = {}

for _, row in df.iterrows():
    symptoms = [
        row['Symptom_1'],
        row['Symptom_2'],
        row['Symptom_3'],
        row['Symptom_4']
    ]
    symptoms = [s for s in symptoms if s]

    disease_symptoms[row['Disease']] = symptoms

# ----------------------------------------
# 4) Build inverted index: symptom → list of diseases
# ----------------------------------------
symptom_to_disease = defaultdict(set)

for disease, symptoms in disease_symptoms.items():
    for s in symptoms:
        symptom_to_disease[s].add(disease)

# ----------------------------------------
# 5) Matching logic
# ----------------------------------------
def match_symptoms(user_symptoms):
    """
    user_symptoms: list of strings from user input
    Returns diseases ranked by symptom match score
    """

    # clean user symptoms
    cleaned = [clean_symptom(s) for s in user_symptoms]
    cleaned = [s for s in cleaned if s]

    disease_scores = defaultdict(int)

    for sym in cleaned:
        # Exact match
        if sym in symptom_to_disease:
            for d in symptom_to_disease[sym]:
                disease_scores[d] += 1
        else:
            # fuzzy partial match
            for known_sym in symptom_to_disease:
                if sym in known_sym or known_sym in sym:
                    for d in symptom_to_disease[known_sym]:
                        disease_scores[d] += 0.5  # weaker match

    # Sort diseases based on score
    ranked = sorted(disease_scores.items(), key=lambda x: -x[1])

    return ranked

# ----------------------------------------
# 6) USER INPUT (4 symptoms)
# ----------------------------------------
if __name__ == "__main__":
    print("\n=== Rule-Based Symptom Checker ===")
    s1 = input("Enter symptom 1: ")
    s2 = input("Enter symptom 2: ")
    s3 = input("Enter symptom 3: ")
    s4 = input("Enter symptom 4: ")

    user_input = [s1, s2, s3, s4]

    results = match_symptoms(user_input)

    print("\nInput Symptoms:", user_input)
    print("\nPossible Diseases (ranked):")

    if not results:
        print("No matches found.")
    else:
        for disease, score in results[:10]:
            print(f"{disease}  --> score: {score}")
