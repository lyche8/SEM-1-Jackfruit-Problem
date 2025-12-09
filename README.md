PROJECT NOTES (Private Repository)

This repo contains my personal Python scripts for:

1)Symptom Checker

2)BMI Calculator (Male/Female Classification)

3)To analyze age groups 

4)Appointment Token Generator

2 and 3 use CSV files for reading/writing data.

FILES IN THIS REPO-

symptom_checker.py

bmi_calculator.py

appointment_token_generator.py

data/

    symtoms_df.csv
    Hospital_data_completed.csv

output/

    appointments.csv

1. Symptom Checker (symptom_checker.py)
   
Uses a CSV of symptoms/labels. Predicts condition for given symptoms.

Run:

python symptom_checker.py

2. BMI Calculator (bmi_calculator.py)
   
Takes weight (kg), height (cm), and gender. Male/female BMI categories handled separately (as per WHO logic). Calculates BMI and category.

Run:

python bmi_calculator.py

3.To analyze age groups

Analyzes hospital patient data by grouping ages, calculating averages for spending and visits, and showing insurance distribution. Also visualizes patient counts by age group with a simple bar chart.

4. Appointment Token Generator (appointment_token_generator.py)
   
Creates a unique token each time. Saves tokens to output/appointments.csv.

Run:

python appointment_token_generator.py
