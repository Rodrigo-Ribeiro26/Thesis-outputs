import pandas as pd
import os

# Specify the folder where your TSV files are located
folder_path = "D:/Mestrado/Tese/Outputs/tsvs_1"

# Get a list of TSV file names in the folder
tsv_files = [f for f in os.listdir(folder_path) if f.endswith(".tsv")]

# Create an empty DataFrame to hold the merged data
merged_data = pd.DataFrame()

# Iterate through TSV files and merge data
for file in tsv_files:
    # Read the TSV file into a DataFrame
    data = pd.read_csv(os.path.join(folder_path, file), sep='\t')
    
    # Add a column for the file name
    data['FileName'] = file
    
    # Merge the data into the merged_data DataFrame, filling missing values with 0
    if merged_data.empty:
        merged_data = data
    else:
        merged_data = pd.merge(merged_data, data, on='FileName', how='outer')

# Sort the rows alphabetically based on the 'FileName' column
merged_data.sort_values(by='FileName', inplace=True)

# Remove the 'FileName' column (if not needed)
merged_data.drop(columns=['FileName'], inplace=True)

# Fill missing values with 0
merged_data = merged_data.fillna(0)

# Save the merged data to an Excel file
merged_data.to_excel("output_2.xlsx", index=False)