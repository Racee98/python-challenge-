import os
import csv
import win32com.client as win32

# Path to the VBA script file
vba_script_path = os.path.join('VBA_script.txt')

# Path to the stock data CSV file
csv_path = os.path.join('stock_data.csv')

# Create an Excel application object
excel = win32.gencache.EnsureDispatch('Excel.Application')

# Open the stock data workbook
workbook = excel.Workbooks.Open(os.path.abspath(csv_path))

# Run the VBA script on every worksheet in the workbook
for sheet in workbook.Worksheets:
    # Activate the worksheet
    sheet.Activate()

    # Run the VBA script
    excel.Application.Run("'" + os.path.abspath(vba_script_path) + "'!ProcessStockData")

# Save and close the workbook
workbook.Save()
workbook.Close()

# Quit Excel
excel.Quit()

# Path to the VBA script output file
vba_output_path = os.path.join('VBA_script_output.csv')

# Read the VBA script output file
with open(vba_output_path, 'r') as vba_output_file:
    # Parse the CSV data
    csv_reader = csv.reader(vba_output_file)
    for row in csv_reader:
        # Process and print each row of data as desired
        ticker_symbol = row[0]
        yearly_change = row[1]
        percent_change = row[2]
        total_volume = row[3]
        print(f'Ticker Symbol: {ticker_symbol}')
        print(f'Yearly Change: {yearly_change}')
        print(f'Percent Change: {percent_change}')
        print(f'Total Volume: {total_volume}')
        print('-----------------------------')

        # Additional logic for finding greatest % increase, % decrease, and total volume

        # ...

# Clean up the VBA script output file
os.remove(vba_output_path)
