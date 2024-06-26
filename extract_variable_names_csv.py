import pandas as pd

def extract_variable_names():
    # Hardcoded paths for the CSV file and the output file
    csv_file_path = 'datasets/NSUMHSS_2022_PUF_CSV.csv'
    output_file_path = 'nsumhss_variables.txt'

    # Load the CSV file
    data = pd.read_csv(csv_file_path)

    # Extract the column names (variable names)
    variable_names = data.columns.tolist()

    # Save the variable names to a text file
    with open(output_file_path, 'w') as file:
        for name in variable_names:
            file.write(name + '\n')

if __name__ == "__main__":
    extract_variable_names()
