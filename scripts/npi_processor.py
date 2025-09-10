import polars as pl
import pandas as pd
import time

npi_file_path = "input/npidata.csv"

## just load the first 1000 rows
start_time_polars = time.time()
df_polars = pl.read_csv(npi_file_path) #, n_rows=1_000_000)
end_time_polars = time.time()
elapsed_time_polars = end_time_polars - start_time_polars
print(elapsed_time_polars)


start_time_pandas = time.time()
df_pandas = pd.read_csv(npi_file_path, nrows=1000000, low_memory=False)
end_time_pandas = time.time()
elapsed_time_pandas = end_time_pandas - start_time_pandas
print(elapsed_time_pandas)

# validate data
missing_npi = df_pandas['NPI'].isnull().sum()
df_pandas

if missing_npi > 0:
    print(f"Warning: {missing_npi} rows with missing NPI found.")

# create output csv 
output_path = "output/npi_processed.csv"
df_pandas.to_csv(output_path, index=False)
print(f"NPI data successfully saved to: {output_path}")

