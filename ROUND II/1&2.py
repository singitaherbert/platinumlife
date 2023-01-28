import pandas as pd  # dependency
import numpy as np  # dependency
df_teacher = pd.DataFrame({
    "name": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinadine Zidane"],
    "married": [True, True, False, True],
    "school": ["Manchester High School", "Liverpool High School", "Arsenal High", np.nan]
})

df_student = pd.DataFrame({
    "teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola", "Pep Guardiola", "Mikel Arteta"],
    "name": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino",
             "Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "Thomas Partey"],
    "age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
    "height": ['2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m']
})

df_teacher_copy = df_teacher.copy()
df_student_copy = df_student.copy()
df_teacher_json = df_teacher.to_json()
df_student_json = df_student.to_json()
combined_df = pd.merge(df_teacher_copy, df_student_copy,
                       left_on="name", right_on="teacher")
combined_df = combined_df.to_json(orient='records', indent=2)
print(combined_df)
# new_df = pd.json_normalize(combined_df,'teacher','married','school',[['name','age','height']])
# print(new_df)


# Part B

df_student = pd.DataFrame({
    "teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola", "Pep Guardiola", "Mikel Arteta"],
    "name": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino", "Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "ThomasPartey"],
    "age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
    "height": ['2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m'],
    "weight": ['80kg', '70kg', '690kg', '73kg', '60kg', '70kg', '80kg', '88kg', '74kg',]
})

df_teacher_copy = df_teacher.copy()
df_student_copy = df_student.copy()
df_teacher_json = df_teacher.to_json()
df_student_json = df_student.to_json()
combined_df = pd.merge(df_teacher_copy, df_student_copy,
                       left_on="name", right_on="teacher")
combined_df = combined_df.to_json(orient='records', indent=2)
print(combined_df)
# new_df = pd.json_normalize(combined_df,'teacher','married','school',[['name','age','height']])
# print(new_df)
