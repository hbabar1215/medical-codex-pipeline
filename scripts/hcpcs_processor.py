import os
import pandas as pd

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

# remove white space from column names
pd.set_option('display.max_columns', None)

df = pd.set_option


# indicate if missing values
df= df.notna()


# save as csv file to output directory
input_file_path = "input/HCPC2025_OCT_ANWEB_v2.txt"
output_file_path = "output/hcpcs_processed_2025.csv"
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
hcpcs_df = load_hcpcs_data(input_file_path)
hcpcs_df.to_csv(output_file_path, index=False)

print(f"HCPCS data successfully saved to: {output_file_path}")
