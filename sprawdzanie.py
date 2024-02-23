#nieaktualne => użyj 2.py potem na wyniku wynik.py

import pandas as pd

# Define the file paths for the provided Excel files
dane_file_path = '/mnt/data/dane.xlsx'
wykaz_file_path = '/mnt/data/wykaz.xlsx'

# Define the function to process the files
def process_excel_files(dane_path, wykaz_path):
    # Read the Excel files into DataFrames
    dane_df = pd.read_excel(dane_path)
    wykaz_df = pd.read_excel(wykaz_path)
    
    # Check if the required columns 'Bezeichnung' in dane_df and 'Zeinr' in wykaz_df exist
    if 'Bezeichnung.............................' in dane_df and 'Zeinr' in wykaz_df:
        # Rename the column in dane_df for consistency
        dane_df.rename(columns={'Bezeichnung.............................': 'Bezeichnung'}, inplace=True)
    
        # Initialize a new column in wykaz_df
        wykaz_df['technologia_ze_starego'] = None
        
        # Iterate over wykaz_df to find matches and update 'technologia_ze_starego'
        for index, wykaz_row in wykaz_df.iterrows():
            if wykaz_row['TYP'] == 'ZŁOŻENIE':
                # Find matching row in dane_df
                match = dane_df[(dane_df['Bezeichnung'] == wykaz_row['Bezeichnung']) & 
                                (dane_df['Zeinr'] == wykaz_row['Zeinr'])]
                
                # If match is found, update the 'technologia_ze_starego' column
                if not match.empty:
                    wykaz_df.at[index, 'technologia_ze_starego'] = match['TECHNOLOGIA'].iloc[0]
    
        # Write the modified wykaz_df to a new Excel file
        output_path = '/mnt/data/wynik.xlsx'
        wykaz_df.to_excel(output_path, index=False)
        
        return output_path

# Attempt to process the files and capture any exceptions
try:
    output_file_path = process_excel_files(dane_file_path, wykaz_file_path)
except Exception as e:
    output_file_path = str(e)

output_file_path
