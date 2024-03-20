import pdb

def es_maximo(sublista, lista_de_listas):
    return sublista == max(lista_de_listas, key=max)

def maximos_por_lista(lista_de_listas):
    pdb.set_trace()  # Punto de parada antes de la comprensión de listas
    return list(filter(lambda sublista: es_maximo(sublista, lista_de_listas), lista_de_listas))

lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
print(maximos_por_lista(lista))

#Conclusión:
#maximos_por_lista para que devuelva verdadero o falso dependiendo de si una lista es el máximo o no. 
#Luego,podemos utilizar filter para filtrar las sublistas que son máximas en la lista de listas.