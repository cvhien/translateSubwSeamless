# import module 
import openpyxl 
  
# load excel with its path 
wrkbk = openpyxl.load_workbook("Sample.xlsx") 
  
sh = wrkbk.active 
  
# iterate through excel and display data 
for row in sh.iter_rows(min_row=5, min_col=3, max_row=23, max_col=3): 
    for cell in row: 
        print(cell.value, end=" ") 
    print() 

