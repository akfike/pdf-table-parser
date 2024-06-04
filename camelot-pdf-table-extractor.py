import camelot

# Specify the path to your PDF file
pdf_path = "pdfs/NSDUH-2022-DS0001-info-codebook (1).pdf"

# Extract tables using stream mode (for tables without borders)
tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream')

# Print the tables or save them to CSV files
for i, table in enumerate(tables):
	print(f"Table {i}")
	print(table.df)
	table.to_csv(f"camelot_table_{i}.csv")