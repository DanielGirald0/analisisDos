import pandas as pd
from data.apartamentos import apartamento1, apartamento2
from helpers.crearTablasHTML import crearTabla

#CREAR DATA FRAME   (pandas siempre retorna un dataframe)

tabla1=pd.DataFrame(apartamento1, columns=['edades'])
tabla2=pd.DataFrame(apartamento2, columns=['edades'])
tabla3=pd.read_csv("./data/empleados.csv")

#.....efectuando filtros con python......

# 1. definir condicion logica que me permita definir un filtro en especifico
empleadosJovenesAnalista1=tabla3.query('edad>28 and cargo == "analista1"')
empleadoSalarioBajo=tabla3.query('salario<5000000 and cargo=="analista2"')
empleadosADespedir=tabla3.query('edad>=50')

# 2. creamos la tabla html con el dataframe del filtro 
crearTabla(empleadosJovenesAnalista1, 'tablaJovenes')
crearTabla(empleadoSalarioBajo, 'tablaSalarioBajos')
crearTabla(empleadosADespedir, 'tablaDespedir')

