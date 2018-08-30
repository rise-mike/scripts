from datetime import datetime
import xlsxwriter

# Create a workbook object (brand new file), as well as a worksheet object.  
wb = xlsxwriter.Workbook('expenses01.xlsx')
ws = wb.add_worksheet("TestName")

### Formats to be applied to every applicable `write` line
bold = wb.add_format({'bold': True})
# Lookup this formatting, I THINK it's the same syntax as custom formats in excel
money_fmt = wb.add_format({'num_format': '$#,##0'})
date_fmt = wb.add_format({'num_format': 'mmm d yyyy'})

# To manually adjust a column width - this accesses a column by index, but you could use 'B:B' instead, 15
# the desired point size
ws.set_column(1,1,15)

## Create header rows, formatting is added as a third parameter
ws.write('A1', 'Item', bold)
ws.write('B1', 'Date', bold)
ws.write('C1', 'Cost', bold)

expenses = (
    ['Rent', '2013-01-13', 1000],
    ['Gas',  '2013-01-14',  100],
    ['Food', '2013-01-16',  300],
    ['Gym',  '2013-01-20',   50],
)

row = 1
col = 0

for item, date_str, cost in expenses:
  date = datetime.strptime(date_str, "%Y-%m-%d")
  ws.write(row, col, item)
  ws.write(row, col + 1, date, date_fmt)
  ws.write(row, col + 2, cost, money_fmt)
  row += 1

ws.write(row, 0, 'Total', bold)
ws.write(row, 2, '=SUM(C2:C5)', money_fmt)

wb.close()