import pandas as pd 
import os

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

## Input/Loinc.csv
input_file_path = "input/Loinc.csv"

# Load LOINC data
try:
    df = pd.read_csv("input/loinc.csv")
except FileNotFoundError:
    print("ERROR: LOINC input file not found. Please place it in the input folder.")
loinc = df.copy()

# Info to describe
loinc.info()

### Strings 
loinc.STATUS.value_counts()

### print first row
loinc.iloc[0]

#### Check potential column names that we think we want to keep: LOINC_NUM, DefinitionDescription
loinc.LOINC_NUM
loinc.LONG_COMMON_NAME

list_cols = ['LOINC_NUM', 'LONG_COMMON_NAME']

loinc_processed = loinc[['LOINC_NUM', 'LONG_COMMON_NAME']]
loinc_processed = loinc[list_cols]

## rename colummns: code, description, last_updated
loinc_processed = loinc_processed.rename(columns={
    'LOINC_NUM': 'code',
    'LONG_COMMON_NAME': 'description'
})

# Create last_updated column 
loinc_processed['last_updated'] = pd.to_datetime('today').strftime('%Y-%m-%d')

# Remove whitespace from column names
df.columns = df.columns.str.strip()

# Indicate if missing values 
print(df.isnull().sum())

# create output file path
output_file_path = "output/loinc_processed.csv"

# Save to CSV
loinc_processed.to_csv(output_file_path, index=False)

