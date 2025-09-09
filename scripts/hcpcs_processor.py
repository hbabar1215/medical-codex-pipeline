import os
import pandas as pd

# 1. Script folder
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Input file path (relative to script folder)
hcpcs_file = os.path.join(script_dir, "..", "input", "HCPC2025_OCT_ANWEB_v2.txt")

# 3. Output folder (project root /output)
output_folder = os.path.join(script_dir, "..", "output")
os.makedirs(output_folder, exist_ok=True)

# 4. Output CSV path
hcpcs_output = os.path.join(output_folder, "hcpcs_processed.csv")

# 5. Check if input file exists
print("Looking for HCPCS file at:", hcpcs_file)
if not os.path.exists(hcpcs_file):
    raise FileNotFoundError(f"Input file not found: {hcpcs_file}")

# 6. Load HCPCS fixed-width file
colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
column_names = ["Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"]

df_hcpcs = pd.read_fwf(hcpcs_file, colspecs=colspecs, names=column_names)

# 7. Save CSV
df_hcpcs.to_csv(hcpcs_output, index=False)
print(f"HCPCS data loaded successfully. Output saved to: {hcpcs_output}")

# 8. Show first 5 rows for verification
print("First 5 rows:")
print(df_hcpcs.head())

# 9. Save only codes to a separate text file
codes_output = os.path.join(output_folder, "hcpcs_codes.txt")
