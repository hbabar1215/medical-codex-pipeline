import pandas as pd


import os

input_path = "input\icd102019syst_codes.txt"  # adjust for your file

if os.path.exists(input_path):
    print(f"File found: {input_path}")
else:
    print(f"File NOT found: {input_path}")

  
# Load the data
file_path = "input\icd102019syst_codes.txt"

columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

df = pd.read_csv(file_path, sep=';', header=None, names=columns)

# clean and process the data
df['code'] = df['code'].str.strip()
df['title_en'] = df['title_en'].str.strip()
df['detailed_title'] = df['detailed_title'].str.strip()
df = df[['code', 'title_en', 'detailed_title']]

# validate data
missing_codes = df['code'].isnull().sum()
if missing_codes > 0:
    print(f"Warning: {missing_codes} rows with missing codes found.")
df = df[df['code'].notnull()]
df = df[df['code'].str.len() > 0]
df['code'] = df['code'].str.upper()
df['title_en'] = df['title_en'].str.title()
df['detailed_title'] = df['detailed_title'].str.title()
df = df.drop_duplicates(subset=['code'])

# save to csv
output_path = "output/icd10who_processed_2019.csv"
df.to_csv(output_path, index=False)
print(f"ICD-10-WHO data successfully saved to: {output_path}")
