# Importando arquivos simples com Pandas

#pip install openpyxl

# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = 'C:/Users/lucasMartins/Documents/DataCamp/importando dados/titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())


# EXCEL

# Assign spreadsheet filename: file
file = 'C:/Users/lucasMartins/Documents/DataCamp/importando dados/battledeath.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print(xls.sheet_names)

# Importando arquivos SAS

# Import sas7bdat package
from sas7bdat import SAS7BDAT


# Save file to a DataFrame: df_sas
with SAS7BDAT('C:/Users/lucasMartins/Documents/DataCamp/importando dados/sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())


# Importando arquivos HDFS

# Import packages
import numpy as np
import h5py

# Assign filename: file
file = 'C:/Users/lucasMartins/Documents/DataCamp/importando dados/L-L1_LOSC_4_V1-1126259446-32.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)
