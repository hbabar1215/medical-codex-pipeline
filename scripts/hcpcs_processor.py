import os
import pandas as pd

# Load the data
try:
    input_file_path = "input/HCPC2025_OCT_ANWEB_v2.txt"
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"ERROR: HCPCS input file not found at {input_file_path}. Please place it in the input folder.")
except FileNotFoundError as e:
    print(e)
    exit(1)

# Function to load HCPCS data
def load_hcpcs_data(file_path):
    """
    Load HCPCS data from a fixed-width formatted text file into a pandas DataFrame.
    
    Args:
        file_path (str): Path to the HCPCS text file.
        
    Returns:
        pd.DataFrame: DataFrame containing the HCPCS data.
    """
    # Define column specifications and names based on the file structure
    colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
    column_names = [
        "Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"
    ]
    
    # Read the fixed-width formatted file into a DataFrame
    df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)
    
    return df

df = load_hcpcs_data(input_file_path)

# Rename columns: code, description, last_updated
df = df.rename(columns={"Code": "code", "Description1": "description"})

# Add a column for last_updated
df['last_updated']= pd.to_datetime('today').strftime('%y-%m-%d')

# Keep only 3 columns in final output
df_new = df[['code', 'description', 'last_updated']]

# Remove white space from column names
df.columns = df.columns.str.strip()

# Indicate if missing values
print(df_new.isnull().sum())

# Save as csv file to output directory
input_file_path = "input/HCPC2025_OCT_ANWEB_v2.txt"
output_file_path = "output/hcpcs_processed_2025.csv"
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
df_new.to_csv(output_file_path, index=False)

print(f"HCPCS data successfully saved to: {output_file_path}")

# print shape of data
print(df_new.head())
print(df_new.shape)
