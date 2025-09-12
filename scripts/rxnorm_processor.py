import polars as pl
from pathlib import Path
import time
import logging

# https://www.nlm.nih.gov/research/umls/rxnorm/docs/techdoc.html#s12_10

# Load the data
file_path = Path('input/RXNATOMARCHIVE.RRF')
try:
    if not file_path.exists():
        raise FileNotFoundError(f"ERROR: RXNATOMARCHIVE.RRF input file not found at {file_path}. Please place it in the input folder.")
except FileNotFoundError as e:
    print(e)
    exit(1)

# Define column names based on the RXNATOMARCHIVE.RRF structure
columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]

# Read the RXNATOMARCHIVE.RRF file using Polars
df = pl.read_csv(
    file_path,
    separator='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True
)

# Drop the existing 'code' column
if 'code' in df.columns:
    df = df.drop('code')

# Rename columns to code, description, last_updated
renamed_columns = {
    'rxaui': 'code',
    'str': 'description',
}
df = df.rename(renamed_columns)

# Add a last_updated column 
df = df.with_columns(
    pl.lit(time.strftime('%Y-%m-%d')).alias('last_updated'))

# Load only the code, description, last_updated columns in final ouput
df = df.select(["code", "description", "last_updated"])

# Remove whitespace from column names
df = df.rename({col: col.strip() for col in df.columns})

# Indicate if missing values
print(df.null_count())

# Ensure output directory exists
output_dir = Path('output')
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'RXNATOMARCHIVE.csv'

# Save to CSV
df.write_csv(output_path)

# Use logging to log the success message
import logging
logging.info(f"RXNATOMARCHIVE data successfully saved to {output_path}")

# Print summary
print(f"Successfully parsed {len(df)} records from RXNATOMARCHIVE.RRF")
print(f"Saved to {output_path}")
print(f"Dataset shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")