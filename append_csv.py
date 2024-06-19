import pandas as pd

# Load the first CSV file
csv1 = pd.read_csv('consolidated_nsduh_data_main.csv')

# Load the second CSV file
csv2 = pd.read_csv('consolidated_nsduh_data.csv')

combined_csv = pd.concat([csv1, csv2], ignore_index=True)

# Save the combined CSV to a new file
combined_csv.to_csv('consolidated_nsduh_data_main.csv', index=False)
