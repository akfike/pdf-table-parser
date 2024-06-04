import camelot
import matplotlib.pyplot as plt # this to add
from ctypes.util import find_library
print(find_library("gs"))

# Specify the path to your PDF file
pdf_path = "pdfs/NSDUH-2022-DS0001-info-codebook (1).pdf"

# Extract tables using stream mode (for tables without borders)
tables = camelot.read_pdf(pdf_path, pages='529,528,48', flavor='stream', edge_tol=1000)

# # Print the tables or save them to CSV files
for i, table in enumerate(tables):
	print(f"Table {i}")
	print(table.parsing_report)
	camelot.plot(table, kind='contour') # text, grid, contour, line, joint, 
	plt.show()
	print(table.df)
	table.to_csv(f"camelot_table_{i}.csv")
	input("Type N for next")