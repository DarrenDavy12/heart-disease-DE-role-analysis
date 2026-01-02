## Heart Disease Analysis 🩺 ❤️

## Overview

This mini-project demonstrates a **data engineering workflow** using Python and Pandas. The goal is to process and analyze a healthcare dataset (`Heart_Disease_Analysis.csv`) to extract meaningful insights, while applying best practices for **data ingestion, cleaning, transformation, and aggregation**.

The project focuses on:

- Loading CSV data into Python
- Inspecting and understanding the dataset
- Standardizing column names for clarity and safety
- Aggregating and summarizing patient data
- Producing clean, report-ready outputs
- Applying pipeline thinking suitable for data engineering roles

---

## Dataset

The dataset used is the **Heart Disease Prediction dataset**, containing medical records for patients.  

Each row represents **one patient record**, and columns include attributes such as:

- `age`, `sex`, `chest_pain_type`, `blood_pressure`, `cholesterol`
- `fbs_over_120`, `ekg_results`, `max_heart_rate`, `exercise_angina`
- `st_depression`, `st_slope`, `num_vessels_fluro`, `thallium`
- `heart_disease` (target variable: Presence / Absence)

---

## Project Steps

### 1. Load and Inspect CSV

```python
import pandas as pd

heart_df = pd.read_csv('Heart_Disease_Analysis.csv')
print(heart_df.head())   # preview first 5 rows
print(heart_df.info())   # inspect data types and nulls



2. Standardize Column Names

Column names were cleaned and standardized for safer transformations and better readability:

heart_df = heart_df.rename(columns={
    'Age' : 'age',
    'Sex' : 'sex',
    'Chest pain type' : 'chest_pain_type',
    'BP' : 'blood_pressure',
    'Cholesterol' : 'cholesterol',
    'FBS over 120' : 'fbs_over_120',
    'EKG results' : 'ekg_results',
    'Max HR' : 'max_heart_rate',
    'Exercise angina' : 'exercise_angina',
    'ST depression' : 'st_depression',
    'Slope of ST' : 'st_slope',
    'Number of vessels fluro' : 'num_vessels_fluro',
    'Thallium': 'thallium',
    'Heart Disease': 'heart_disease'
})



3. Count Patients by Heart Disease Status


patient_with_disease_count = heart_df.groupby('heart_disease').size().reset_index(name='patient_count')
print(patient_with_disease_count)



4. Average Age Among Patients With Heart Disease

disease_df = heart_df[heart_df['heart_disease'] == 'Presence']
average_age = disease_df['age'].mean()
print(average_age)



5. Average Age by Sex for Patients With Heart Disease

average_sex_with_heart_disease = disease_df.groupby('sex')['age'].mean().reset_index(name='avg_age')
print(average_sex_with_heart_disease)




6. Aggregated Pipeline: Patient Counts and Average Age

aggregated_heart_df = heart_df.groupby(['heart_disease', 'sex']).agg(
    patient_count=('age', 'count'),
    average_age=('age', 'mean')
).reset_index()

print(aggregated_heart_df)



# Key teachings I took:

How to ingest, clean, and explore CSV datasets in Python

How to standardize column names for safer downstream usage

Filtering rows with boolean masks (df[df['column'] == value])

Grouping and aggregating data using .groupby() and .agg()

Resetting index and producing clean summary tables

Thinking like a data engineer: step-by-step pipeline creation and output production
