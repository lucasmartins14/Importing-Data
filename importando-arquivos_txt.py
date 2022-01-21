# Importando arquivos de texto

import pandas as pd

# Open a file: file
file = open("C:/Users/lucasMartins/Documents/DataCamp/importando dados/ohobbit.txt", mode="r")

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)