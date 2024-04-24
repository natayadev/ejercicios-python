import pandas as pd

#Recomendado utilizar el path relativo
path_relativo_csv = 'ejercicios/data/padron.csv'
path_relativo_excel = 'ejercicios/data/padron.xlsx'
#path_absoluto = 'C:\Users\nflores\Desktop\clase\ejercicios\data\padron.csv'

# Lectura de un csv
data_csv = pd.read_csv(path_relativo_csv)
print(data_csv)

# Lectura de un excel
data_excel = pd.read_excel(path_relativo_excel)
print(data_excel)