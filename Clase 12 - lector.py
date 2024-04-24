import csv
path = 'data/lorem.txt'

with open(path, 'r') as file:
    contenido = file.read()
#print(contenido)

pathcsv = 'data/data.csv'

with open('data/data.csv', 'r') as file:
    lector = csv.reader(file)
    for fila in lector:
        print(fila)