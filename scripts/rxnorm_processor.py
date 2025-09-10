import polars as pl
from pathlib import Path

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
# remove any leading/trailing whitespace
columns = [col.strip() for col in columns]

# remove missing values in the columns list
columns = [col for col in columns if col]

# Read the RXNATOMARCHIVE.RRF file using Polars
df = pl.read_csv(
    file_path,
    separator='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True
)

# Ensure output directory exists
output_dir = Path('output')
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'RXNATOMARCHIVE.csv'

# Save to CSV
df.write_csv(output_path)

# Print summary
print(f"Successfully parsed {len(df)} records from RXNATOMARCHIVE.RRF")
print(f"Saved to {output_path}")
print(f"Dataset shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")