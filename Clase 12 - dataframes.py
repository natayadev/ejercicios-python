import pandas as pd

# Definimos dos DataFrames
df_alumnos = pd.DataFrame({
    'Alumno': ['Alicia', 'Agustina', 'Carlos', 'David', 'Fernando'],
    'Edad': [8, 9, 9, 10, 9]
})

df_notas = pd.DataFrame({
    'Alumno': ['Alicia', 'Agustina', 'Carlos', 'David','Fernando','Evelin', 'Alicia', 'Carlos', 'Evelin'],
    'Nota': [8, 3, 7, 8, 2, 10, 6, 9, 10]
})

# Agrupación de tablas por Nota
grouped_df = df_notas.groupby("Nota").count()
print(grouped_df)

# Reorganizar nuestro DataFrame con pivot_table
pivot_df = df_notas.pivot_table("Nota", index="Alumno", aggfunc="mean")
print(pivot_df)

# Combinación de tablas externa por Alumnos
merged_df = pd.merge(df_alumnos, df_notas, on="Alumno", how="outer")
print(merged_df)

# Apply y normalización de columna
def aprobados(nota):
    return 'Aprobado' if nota >= 6  else 'Desaprobado'
    
merged_df['Estado'] = merged_df['Nota'].apply(aprobados)
print(merged_df)

merged_df = merged_df.dropna() # Eliminamos NaN
merged_df['Edad'] = merged_df['Edad'].round().astype(int)

print(merged_df)