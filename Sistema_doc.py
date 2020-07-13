import pandas as pd
from tabulate import tabulate
import os

#Obtener dataframe de archivo excel con los nombres de ficha
df = pd.read_excel("Ficha_Master.xlsx", sheet_name="Fichas", header=0)

#Recorrido por filas de dataframe
for i, row in df.iterrows():
	tabla = tabulate(row.to_frame(), tablefmt='rst')
	print(tabla, type(tabla))
	archivo = open('tabla.rst', 'w')
	archivo.write(tabla)
	archivo.close()
	break