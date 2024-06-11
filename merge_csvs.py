import pandas as pd

# Load the two CSV files
descriptions_csv_path = 'csvs/variable_descriptions.csv'
consolidated_csv_path = 'consolidated_nsduh_data_1.csv'

print(f"Loading descriptions CSV file from {descriptions_csv_path}")
descriptions_df = pd.read_csv(descriptions_csv_path)
print(f"Descriptions CSV loaded successfully with {len(descriptions_df)} records")

print(f"Loading consolidated CSV file from {consolidated_csv_path}")
consolidated_df = pd.read_csv(consolidated_csv_path)
print(f"Consolidated CSV loaded successfully with {len(consolidated_df)} records")

# Merge the two DataFrames on variable_name == Question_Code
merged_df = pd.merge(consolidated_df, descriptions_df[['variable_name', 'description']], left_on='Question_Code', right_on='variable_name', how='left')

# Drop the 'variable_name' column from the merged DataFrame
merged_df.drop(columns=['variable_name'], inplace=True)

# Save the merged DataFrame to a new CSV file
output_file_path = 'csvs/merged_nsduh_data.csv'
print(f"Saving merged data to {output_file_path}")
merged_df.to_csv(output_file_path, index=False)
print("Merged data saved successfully")

# Print the merged DataFrame
print(merged_df.head())
