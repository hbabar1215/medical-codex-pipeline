import os
import pandas as pd

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
def load_icd10cm_data(file_path):
    """
    Load ICD-10-CM data from a fixed-width formatted text file into a DataFrame.
    """
    colspecs = [(0, 7), (7, 107), (107, 110), (110, 113), (113, 116), (116, 119), (119, 122), (122, 125)]
    column_names = ["Code", "Description", "Category", "Subcategory", "Invalid1", "Invalid2", "Invalid3", "Invalid4"]
    
    # Read the fixed-width formatted file into a DataFrame
    df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)
    return df

# Load the data
df = load_icd10cm_data(input_file)

# Optional: inspect data
print("Columns in df:", df.columns)
print(df.head())

# Save to CSV
df.to_csv(output_file, index=False)
print(f"ICD-10-CM data successfully saved to: {output_file}")
    





