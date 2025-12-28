# The CSV to Data Engineer Playbook using Python and Pandas 

import pandas as pd 


# fetch and read csv 

heart_df = pd.read_csv('Heart_Disease_Analysis.csv')

print(heart_df.head())                   # show first 5 rows
print(heart_df.info()) 




# Standardised columns (clean-up)

# I standardised column names early to make transformations safer and downstream usage easier. 


heart_df = heart_df.rename(columns={
    'Age' : 'age',
    'Sex' : 'sex',
    'Chest pain type' : 'chest_pain_type',
    'BP' : 'blood_pressuer',
    'Cholesterol' : 'cholesterol',
    'FBS over 120' : 'fbs_over_20',
    'EKG results' : 'ekg_results',
    'Max HR' : 'max_heart_rate',
    'Exercise anigima' : 'exercise_animga',
    'ST depression' : 'st_depression',
    'Slope of ST' : 'st_slope',
    'Number of vessels fluro ' : 'num_vessels_fluro',
    'Thallium': 'thallium',
    'Heart Disease': 'heart_disease'

})


# How many patients have heart disease vs not?

patient_with_disease_count = heart_df.groupby('heart_disease').size().reset_index(name='patient_count')
print(patient_with_disease_count)





# Among patients WITH heart disease, what is the average age?

disease_df = heart_df[heart_df['heart_disease'] == 'Presence']          # filter patients with heart disease
average_age = disease_df['age'].mean()                                  # then find average age 
print(average_age)




# Average age of patients by sex for patients with heart disease

disease_df = heart_df[heart_df['heart_disease'] == 'Presence']          # filter patients with heart disease
average_sex_with_heart_disease = heart_df.groupby('sex')['age'].mean().reset_index(name='avg_age')     # group by sex and then find average age of group
print(average_sex_with_heart_disease)





# Goal: Produce a CSV showing:                      heart_disease	    sex	       patient_count	    average_age


# use '.agg' when using multiple aggregations
# 'mean' is avg in python 
# 'reset_index' means reset columns back in the end

aggregated_heart_df = heart_df.groupby(['heart_disease', 'sex']).agg(
    patient_count = ('age', 'count'),
    average_age = ('age', 'mean')
).reset_index()

print(aggregated_heart_df)

