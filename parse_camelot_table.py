import pandas as pd
import re
import glob

# Function to extract the short description
def extract_short_description(description):
    """Extract the short description after the pattern 'Len : #'."""
    match = re.search(r'Len : \d+(.+)', description)
    if match:
        return match.group(1).strip()
    return ''

# Function to parse camelot table CSV files
def parse_camelot_table_v6(camelot_table):
    # Drop rows with all NaN values
    camelot_table.dropna(how='all', inplace=True)

    # Initialize lists to store extracted data
    question_codes = []
    short_descriptions = []
    related_variables = []
    answer_codes = []
    answer_meanings = []

    current_question_code = None
    current_short_description = None
    current_related_variables = None

    # Iterate through the rows of the camelot table
    for index, row in camelot_table.iterrows():
        if pd.notna(row[0]) and not row[0].startswith('(') and not row[0].startswith('\\n'):
            current_question_code = row[0]
            current_short_description = extract_short_description(row[1] if pd.notna(row[1]) else '')
        elif pd.notna(row[0]) and row[0].startswith('('):
            current_related_variables = row[0]
        elif pd.notna(row[1]) and '=' in row[1]:
            code_meaning_split = row[1].split('=')
            code = code_meaning_split[0].strip()
            meaning = code_meaning_split[1].split('.....')[0].strip()
            question_codes.append(current_question_code)
            short_descriptions.append(current_short_description)
            related_variables.append(current_related_variables)
            answer_codes.append(code)
            answer_meanings.append(meaning)
        elif current_question_code:
            question_codes.append(current_question_code)
            short_descriptions.append(current_short_description)
            related_variables.append(current_related_variables)
            answer_codes.append('')
            answer_meanings.append('')

    # Create a DataFrame with the extracted data
    parsed_data = pd.DataFrame({
        'Question_Code': question_codes,
        'Short_Description': short_descriptions,
        'Related_Variables': related_variables,
        'Answer_code': answer_codes,
        'Answer_meaning': answer_meanings
    })

    return parsed_data

# Use glob to dynamically load all camelot CSV files
file_paths = glob.glob('csvs/nsduh_table_*.csv')

# Parse all camelot tables
parsed_data_frames = [parse_camelot_table_v6(pd.read_csv(file_path)) for file_path in file_paths]

# Combine all parsed data into a single DataFrame
consolidated_data_v6 = pd.concat(parsed_data_frames, ignore_index=True)

# Save the consolidated DataFrame to a CSV file
consolidated_data_v6.to_csv('consolidated_nsduh_data.csv', index=False)

# Display the consolidated DataFrame
print(consolidated_data_v6)

# Print the specific cell in the DataFrame
print(consolidated_data_v6.iloc[90:91, 4:5])
