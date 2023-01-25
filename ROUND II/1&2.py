#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd #dependency
import numpy as np #dependency
df_teacher = pd.DataFrame({
"name": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinadine Zidane"],
"married": [True, True, False, True],
"school": ["Manchester High School", "Liverpool High School", "Arsenal High", np.nan]
})

df_student = pd.DataFrame({
"teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola","Pep Guardiola","Mikel Arteta"],
"name": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino",
"Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "Thomas Partey"],
"age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
"height": ['2.1m','2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m']
})


# Create a copy of the original dataframes
df_teacher_copy = df_teacher.copy()
df_student_copy = df_student.copy()

# Use the merge function to join the dataframes on the "name" column
merged_df = pd.merge(df_teacher_copy, df_student_copy, left_on="name", right_on="teacher")

# Print the resulting dataframe
print(merged_df)

df_teacher_json = df_teacher.to_json()

# Convert the df_student DataFrame to a JSON object
df_student_json = df_student.to_json()

# Print the resulting JSON objects
# print(df_teacher_json)
print(df_student_json)


# In[ ]:





# In[ ]:




