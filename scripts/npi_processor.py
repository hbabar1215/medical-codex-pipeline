import polars as pl
import pandas as pd
import time
import os

npi_file_path = "input/npidata.csv"
output_path = "output/npi_processed.csv"

# Ensure output directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

try:
    if not os.path.exists(npi_file_path):
        raise FileNotFoundError(f"ERROR: NPI input file not found at {npi_file_path}. Please place it in the input folder.")
except FileNotFoundError as e:
    print(e)
    exit(1)
    
# Load first 1,000,000 rows using Polars
start_time_polars = time.time()
df_polars = pl.read_csv(npi_file_path)  # you can add n_rows=1_000_000 if needed
end_time_polars = time.time()
print("Polars load time:", end_time_polars - start_time_polars)

df_polars_small = df_polars.select([
    'NPI', 
    'Provider Last Name (Legal Name)'
])

## rename colummns: code, description, last_updated
df_polars_small = df_polars_small.rename({
    'NPI': 'code',
    'Provider Last Name (Legal Name)': 'description',
    'last_updated': 'last_updated'
})


# Load first 1,000,000 rows using Pandas
start_time_pandas = time.time()
df_pandas = pd.read_csv(npi_file_path, nrows=1_000_000, low_memory=False)
end_time_pandas = time.time()
print("Pandas load time:", end_time_pandas - start_time_pandas)

# remove unavailable NPIs listed as <UNAVAIL>
df_pandas = df_pandas[df_pandas['NPI'] != '<UNAVAIL>']


# Validate data
missing_npi = df_pandas['NPI'].isnull().sum()
if missing_npi > 0:
    print(f"Warning: {missing_npi} rows with missing NPI found.")

# Save to CSV
df_pandas.to_csv(output_path, index=False)
print(f"NPI data successfully saved to: {output_path}")

