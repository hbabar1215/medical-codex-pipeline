import pandas as pd
import os

# Ensure output directory exists
os.makedirs("output", exist_ok=True)
print("Current working directory:", os.getcwd())

# Load the data
try:
    input_file_path = "input/icd102019syst_codes.txt"
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"ERROR: ICD-10-WHO input file not found at {input_file_path}. Please place it in the input folder.")
except FileNotFoundError as e:
    print(e)
    exit(1)


columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

df = pd.read_csv(input_file_path, sep=';', header=None, names=columns)

# drop code column in original file to only keep one 
if 'code' in df.columns:
    df = df.drop(columns=['code'])

## rename colummns: code, description, last_updated
df = df.rename(columns={
    'icd10_code': 'code',
    'type': 'description'
})

# add a column for last_updated
df['last_updated'] = pd.to_datetime('today').strftime('%Y-%m-%d')


# keep only 3 columns
df = df[['code', 'description', 'last_updated']]

# Remove whitespace from column names
df.columns = df.columns.str.strip()

# Indicate if missing values 
print(df.isnull().sum())

# save to csv
output_path = "output/icd10who_processed_2019.csv"
df.to_csv(output_path, index=False)
print(f"ICD-10-WHO data successfully saved to: {output_path}")

print (df.head())