import csv

def leer_csv(nombre_archivo):
    datos = []
    with open(nombre_archivo, 'r', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            datos.append(fila)
    return datos

def media_gastos_anual(datos):
    total_gastos = sum(float(fila['Gasto']) for fila in datos)
    return total_gastos / len(datos)

def gasto_total_anual(datos):
    total_gastos = sum(float(fila['Gasto']) for fila in datos)
    return total_gastos

def ingresos_totales_anuales(datos):
    total_ingresos = sum(float(fila['Ingresos']) for fila in datos)
    return total_ingresos

nombre_archivo = 'E:/MASTER/Buenas_practicas/finanzas2020.csv'  
datos = leer_csv(nombre_archivo)
media_gastos = media_gastos_anual(datos)
gasto_total = gasto_total_anual(datos)
ingresos_totales = ingresos_totales_anuales(datos)

print("La media de gastos al año es:", media_gastos)
print("El gasto total a lo largo del año es:", gasto_total)
print("Los ingresos totales a lo largo del año son:", ingresos_totales)
