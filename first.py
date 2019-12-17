import numpy as np

np.busday_count('2019-01-12', '2019-12-31')

def calculo_salario(salarioneto, dias):
    bruto = salarioneto / dias
    return bruto

salarioneto = input("cual es el salario mensual :")
fecha1 = input("cual es la fecha inicial del mes en el formato aaaa-mm-dd :")
fecha2 = input("cual es la fecha final del mes en el formato aaaa-mm-dd :")
dias = np.busday_count(fecha1, fecha2) +1
# diasquincena = input ("cuantos dias tuvo la quincena :")
semana = calculo_salario(int(salarioneto),int(dias))
print(semana)