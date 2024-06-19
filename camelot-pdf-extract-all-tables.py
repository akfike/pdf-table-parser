import camelot
import matplotlib.pyplot as plt
from ctypes.util import find_library
print(find_library("gs")) # Make sure you have ghostscript installed (thru homebrew or other)

# Specify the path to your PDF file
pdf_path = "pdfs/NSDUH-2022-DS0001-info-codebook (1).pdf"

# Extract tables using stream mode (for tables without borders) # 42-598
tables = camelot.read_pdf(pdf_path, pages='497-598', flavor='stream', edge_tol=1000, flag_size=True)

# Function to convert specific columns to strings to avoid automatic date conversion
def convert_columns_to_string(df):
    for col in df.columns:
        df[col] = df[col].astype(str)
    return df


for i, table in enumerate(tables):
    print(f"Table {i}")
    print(table.parsing_report)
    table.df = convert_columns_to_string(table.df)
    table.to_csv(f"csvs/nsduh_table_{i}.csv")