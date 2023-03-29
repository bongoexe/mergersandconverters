import csv
import xlsxwriter

# Replace 'file.tsv' with the path to your .tsv file
# Replace 'file.xlsx' with the desired name for the Excel file
tsv_file = '/Users/leo/Documents/patents database/g_assignee_not_disambiguated.tsv'
excel_file = '/Users/leo/Documents/patents database/fileisambiguo.xlsx'

# Create a new Excel file and add a worksheet
workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet()

# Read in the .tsv file, row by row, and write each row to the Excel worksheet
with open(tsv_file, 'r') as tsv_in:
    tsv_reader = csv.reader(tsv_in, delimiter='\t')
    for row_index, row in enumerate(tsv_reader):
        for col_index, cell in enumerate(row):
            worksheet.write(row_index, col_index, cell)

# Save the Excel file
workbook.close()



