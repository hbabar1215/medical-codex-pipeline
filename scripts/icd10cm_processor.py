import os
import pandas as pd
import re

# Paths
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)

input_file = os.path.join(project_dir, "input", "icd10cm_order_2025.txt")
output_file = os.path.join(project_dir, "output", "icd10cm_processed_2025.csv")
log_file = os.path.join(project_dir, "logs", "icd10cm_processing.log")

# Ensure directories exist
os.makedirs(os.path.dirname(log_file), exist_ok=True)
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Function to load ICD-10-CM data
# Load the data
try:
    input_file_path = "input/icd10cm_order_2025.txt"
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"ERROR: ICD-10-CM input file not found at {input_file_path}. Please place it in the input folder.")
except FileNotFoundError as e:
    print(e)
    exit(1)

    # This initializes a blank list to hold the parsed codes (e.g., individual rows from the text file)
codes = []

with open(input_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.rstrip('\n\r') \
        
    # skip short lines
        if len(line) < 15:
            continue

            # Parse the fixed-length format based on pdf instructions
        order_num = line[0:5].strip()  # Order number, first 6 characters
        code = line[6:13].strip()  # ICD-10-CM code, characters 7-13
        level = line[14:15].strip()  # Level indicator (0 or 1), character 15

            # Parse description and description_detailed that follows
        remaining_text = line[16:]  # Text after position 16
        
        # Split by 4+ consecutive spaces to separate description from description_detailed
        parts = re.split(r'\s{4,}', remaining_text, 1)

            # Extract description and description_detailed
        description = parts[0].strip() if len(parts) > 0 else ""
        description_detailed = parts[1].strip() if len(parts) > 1 else ""

            # Append the parsed data to the codes list
        codes.append({
            'code': code,
            'description': description,
           })

    # create df
    df = pd.DataFrame(codes)

# rename columns: code, description, last_updated
df = df.rename({"code":"code",
 "Description" : "description",
})

# Add a column for today's date
df['last_updated']= pd.to_datetime('today').strftime('%y-%m-%d')

# Remove whitespace from column names
df.columns = df.columns.str.strip()

# Indicate if missing values 
print(df.isnull().sum())

# Save to CSV
df.to_csv(output_file, index=False)
print(f"ICD-10-CM data successfully saved to: {output_file}")
print(df.head())
print(df.shape)






