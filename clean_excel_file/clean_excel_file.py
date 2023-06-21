import pandas as pd
import re

def clean_excel_file(input_file, output_file):
    df = pd.read_excel(input_file)
    
    df_cleaned = df.applymap(lambda x: re.sub('[^a-zA-Z0-9]', '', str(x)))
    
    df_cleaned.to_excel(output_file, index=False)

input_file_path = 'input.xlsx'
output_file_path = 'output.xlsx'

clean_excel_file(input_file_path, output_file_path)

print('Excel file cleaned successfully!')