import pdb
def maximos_por_lista(lista_de_listas):
    pdb.set_trace()  # Punto de parada antes de la comprensión de listas
    return [max(sublista) for sublista in lista_de_listas]

lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
print(maximos_por_lista(lista))


#conclusion:
#Cuando ejecutes el código, se detendrá antes de ejecutar la comprensión de listas en la función maximos_por_lista. 

#En ese punto, se pueden utilizar los comandos de pdb como print, next, step, etc., para inspeccionar variables y controlar la ejecución del programa.

#Por ejemplo, podrías inspeccionar el contenido de lista_de_listas, la lista que contiene las sublistas, para entender qué está pasando exactamente con los datos. Luego, puedes seguir avanzando línea por línea con el comando next, inspeccionando el comportamiento de la comprensión de listas y el resultado final.

#Al utilizar pdb, puedes comprender mejor el flujo de tu programa y detectar posibles errores o problemas en la lógica de tu código.





