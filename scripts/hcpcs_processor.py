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
def save_hcpcs_data(df, output_path):
    """
    Save the HCPCS DataFrame to a CSV file.
    
    Args:
        df (pd.DataFrame): DataFrame containing the HCPCS data.
        output_path (str): Path to save the CSV file.
    """
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Validate DataFrame
    # Check required fields
required_columns = ["Code", "Description1"]
missing_required = hcpcs_df[required_columns].isnull().sum()
print("Missing required fields per column:")
print(missing_required)

# Log rows with missing Codes
missing_codes = hcpcs_df[hcpcs_df['Code'].isnull()]
if not missing_codes.empty:
    print(f"Rows with missing codes: {len(missing_codes)}")

    if missing_required.any():
        print("Warning: Some required fields are missing data.")

    # Trim whitespace and normalize case
hcpcs_df['Code'] = hcpcs_df['Code'].astype(str).str.strip().str.upper()
hcpcs_df['Description1'] = hcpcs_df['Description1'].astype(str).str.strip().str.title()

# Remove rows with invalid codes (example: empty or length != 5/6 characters)
valid_code_mask = hcpcs_df['Code'].str.match(r'^[A-Z0-9]{5,6}$')
invalid_codes = hcpcs_df[~valid_code_mask]
if not invalid_codes.empty:
    print(f"Invalid codes found and removed: {len(invalid_codes)}")

hcpcs_df = hcpcs_df[valid_code_mask]
    
    # Save the DataFrame to a CSV file
df.to_csv(output_path, index=False)  # index=False avoids extra column
print(f"HCPCS data saved to {output_path}") 
if __name__ == "__main__":
    # Example usage
    file_path = "input/HCPC2025_OCT_ANWEB_v2.txt"
    output_path = "output/processed_codes.csv"
    
    # Load HCPCS data
    hcpcs_df = load_hcpcs_data(file_path)
    
    # Save HCPCS data to CSV
    save_hcpcs_data(hcpcs_df, output_path)
    