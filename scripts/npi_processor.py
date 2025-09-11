import polars as pl
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

## add in a last_updated column
df_polars_small = df_polars_small.with_columns(
    pl.lit(time.strftime('%Y-%m-%d')).alias('last_updated')
)

# load only 3 columns: code, description, and last_updated
df = df_polars_small.select(["code", "description", "last_updated"])


# save to csv
df.write_csv(output_path)
print(f"NPI data successfully saved to: {output_path}")

# Save to Parquet using Polars
df.write_parquet("output/npi_processed.parquet")
print("NPI data successfully saved to: output/npi_processed.parquet")

# Show file
print(df.head())
