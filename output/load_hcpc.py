import pandas as pd
import os
print("Current working directory:", os.getcwd())

# Path to the HCPCS text file
file_path = "input\HCPC2025_OCT_ANWEB_v2.txt"

# Read the file into a DataFrame
# The file appears to be fixed-width formatted, so we'll use read_fwf

# You may need to adjust colspecs based on actual column widths
# Here is a simple guess based on the sample
colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
column_names = [
    "Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"
]
df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)


## save as csv to Module1_MedicalCodexes/hcpcs/output
output_path = "scripts\hcpcs\output\hcpcs_2025.csv" 
df.to_csv(output_path, index=False)

with open(output_path, 'w') as outfile:   # open in write mode
    for code in df['Code']:
        outfile.write(code + "\n")

print(f"HCPCS data has been successfully loaded and saved to {output_path}") 

import os
# Make sure output folder exists
os.makedirs("output", exist_ok=True)

# Read input text file into pandas DataFrame
df = pd.read_csv("input/codes.txt", header=None, names=["Code"])

# Write output CSV
df.to_csv("output/processed_codes.csv", index=False)
output_path = "output/processed_codes.csv"
df.to_csv(output_path, index=False)  # index=False avoids extra column
print("HCPCS data saved to output/processed_codes.csv")
df.to_csv(output_path, index=False)
