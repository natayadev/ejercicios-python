import pandas as pd

# Definimos dos DataFrames
df_alumnos = pd.DataFrame({
    'Alumno': ['Alicia', 'Agustina', 'Carlos', 'David', 'Fernando'],
    'Edad': [8, 9, 9, 10, 9]
})
print(df_alumnos)

df_notas = pd.DataFrame({
    'Alumno': ['Alicia', 'Agustina', 'Carlos', 'David'],
    'Nota': [8, 9, 7, 8]
})
print('-------------------')
print(df_notas)

# Imprime los primeros datos del DF
print(df_alumnos.head())

# Imprime los últimos datos del DF
print(df_alumnos.tail())

# Imprime un dato al azar o muestra del DF
print(df_alumnos.sample())

# Combinación de tablas interna por Alumnos
print('-------------------')
merged_df = pd.merge(df_alumnos, df_notas, on="Alumno", how="inner")
print(merged_df)

# Combinación de tablas externa por Alumnos
print('-------------------')
merged_df = pd.merge(df_alumnos, df_notas, on="Alumno", how="outer")
print(merged_df)

# Agrupación de tablas por Nota
print('-------------------')
grouped_df = df_notas.groupby("Nota").count()
print(grouped_df)

# Transposición de tablas
print('-------------------')
melted_df = pd.melt(df_notas)
print(melted_df)
