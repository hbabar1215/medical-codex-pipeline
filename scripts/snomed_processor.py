import polars as pl
from pathlib import Path
import time

file_path = Path('input\sct2_Description_Full-en_US1000124_20250901.txt')
log_file = "logs/snpmed_processor.log"

# load the data
try:
    if not file_path.exists():
        raise FileNotFoundError(f"ERROR: SNOMED CT input file not found at {file_path}. Please place it in the input folder.")
except FileNotFoundError as e:
    print(e)
    exit(1)

# Define column names based on the SNOMED CT Description file structure
df = pl.read_csv(
    file_path,
    separator='\t',
    has_header=True,
    quote_char=None,
    encoding='utf8-lossy',
    truncate_ragged_lines=True,
    dtypes={
        'id': pl.Utf8,
        'effectiveTime': pl.Utf8,
        'active': pl.Int32,
        'moduleId': pl.Utf8,
        'conceptId': pl.Utf8,
        'languageCode': pl.Utf8,
        'typeId': pl.Utf8,
        'term': pl.Utf8,
        'caseSignificanceId': pl.Utf8
    }
)

# rename columns to code, description, last_updated
renamed_columns = {
    'id': 'code',
    'languageCode': 'description',
}
df = df.rename(renamed_columns)

# Add a column with today’s date
df = df.with_columns(
    pl.lit(time.strftime('%Y-%m-%d')).alias('last_updated'))

# Keep only the 3 columns if desired
df = df.select(["code", "description", "last_updated"])

# Ensure output directory exists
output_dir = Path('output')
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'sct2_Description_Full.csv'

df.write_csv(output_path)

# use logging to log the success message
import logging
logging.info(f"SNOMED CT data successfully saved to: {output_path}")

# Print summary
print(f"Successfully parsed {len(df)} records from SNOMED CT file")
print(f"Saved to {output_path}")
print(f"Dataset shape: {df.shape}")
print(f"\nColumn names: {df.columns}")
print(f"\nFirst 5 rows:")
print(df.head())

