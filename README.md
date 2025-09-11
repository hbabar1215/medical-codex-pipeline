# Medical Codex Pipeline

## Overview
This repository contains seven healthcare codexes that we had to standardize and parse into a clean format. The goal is to generate output files in csv/parquet format with 3 columns: code, description, and date last updated. 

Standardize column names across all codexes:
- `code`: The primary identifier
- `description`: Human-readable description
- `last_updated`: Processing timestamp

## To get started I first did the following:

### 1. Cloning the Repository
To get a local copy of this repository on your machine use the following git commands:

```bash
# Clone the repository to local machine
git clone https://github.com/yourusername/medical-codex-pipeline.git

# Navigate into the repository folder
cd medical-codex-pipeline

# Check the status of local repository
git status
```

### 2. Basic Git Commands Needed
```bash
# Check if there are updates to download: 
git pull
```
### 3. Create a virtual environment
python -m venv venv

### 4. Install packages
pip install -r requirements.txt

### 5. Folder Structure
  ```
   medical-codex-pipeline/
   ├── input/
   ├── scripts/
   │   ├── snomed_processor.py
   │   ├── icd10cm_processor.py
   │   ├── icd10who_processor.py
   │   ├── hcpcs_processor.py
   │   ├── loinc_processor.py
   │   ├── rxnorm_processor.py
   │   └── npi_processor.py
   ├── output/
   │   ├── csv/
   ├── utils/
   │   └── common_functions.py
   ├── requirements.txt
   └── README.md

### 6. Understanding .gitignore
The `.gitignore` file is crucial for this course because it tells Git which files to ignore and NOT upload to GitHub. This is especially important for:

#### Why We Use .gitignore:
- **Large Dataset Files**: Medical coding datasets (LOINC, ICD-10, HCPCS) can be 100MB+ and exceed GitHub's file size limits
- **Licensing Concerns**: Some medical datasets have usage restrictions and shouldn't be publicly shared
- **Repository Performance**: Keeps the repository lightweight and fast to clone/download
- **Privacy**: Prevents accidental upload of sensitive data files

#### What We're Ignoring:
Our .gitignore specifically excludes these large medical datasets:
- `input\Loinc.csv` - LOINC laboratory codes (~50MB)
- `input\icd10cm_order_2025.txt` - ICD-10 diagnosis codes
- `input\icd102019syst_codes.txt` - WHO ICD-10 systematic names
- `input\HCPC2025_OCT_ANWEB_v2.txt` - HCPCS procedure codes
- `input\npidata.csv` - NPI Healthcare provider identifiers
- `input\RXNATOMARCHIVE.RRF` - RxNorm medication codes
- `input\sct2_Description_Full-en_US1000124_20250901.txt` - Snomed clinical terminology codes 

## Course Structure

### Module 1: Medical Codexes
Working with standard medical coding systems:
- **ICD-10**: International Classification of Diseases (diagnosis codes)
- **LOINC**: Logical Observation Identifiers Names and Codes (lab tests)
- **HCPCS**: Healthcare Common Procedure Coding System (procedures/supplies)
- **NPI**: National Provider Identifiers
- **RxNorm**: Standard Clinical Drug Vocabulary (medication codes)
- **SNOMED CT**: Systematized Nomenclature of Medicine – Clinical Terms

### Data Sources
Students will need to download these datasets separately from official sources:
- LOINC: https://loinc.org/downloads/
- ICD-10: https://www.cms.gov/medicare/coding-billing/icd-10-codes
- HCPCS: https://www.cms.gov/medicare/coding-billing/hcpcscode

### Tools we used 
- **Python**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **Jupyter Notebooks**: Interactive data exploration
- **Git/GitHub**: Version control and collaboration
- **VS Code**: Code editor

### Common Issues and Solutions
- **Large File Errors**: If Git complains about file sizes, check that your datasets are properly listed in .gitignore
- **Memory Issues**: Large CSV files may require chunked processing in Python
- **Encoding Problems**: Medical data often uses different character encodings (UTF-8, Latin-1)

