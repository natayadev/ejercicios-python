import pandas as pd 
from datetime import datetime

df = pd.read_csv('ventas.csv')
print(df.head(5))
print(df.info())
print(df.describe())

# Uso de LOC
subconjunto_loc = df.loc[df['ciudad'] == 'Granada', ['producto', 'fecha']]
#print(subconjunto_loc)

# Uso de ILOC
subconjunto_iloc = df.iloc[0:10, 2:4]
#print(subconjunto_iloc)

# Trabajo con fechas
#df['dia_semana'] = df['fecha'].apply(lambda x: x.strftime("%A"))
#print(df)

# Fecha actual
now = datetime.now()
print(now)
formatted = now.strftime("%A")
print(formatted)

# Valores Atipicos
NaN: not a number
Null: ausencia de valor
Undefined: no definido
Empty: dataframe vacío
None: ausencia de valor pero tambien de la definición
Zero: cero o 0

variable = 0 dtype int64
variable = Zero dtype Zero