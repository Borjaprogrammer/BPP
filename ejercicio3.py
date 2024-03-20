import pdb

def es_maximo(sublista, lista_de_listas):
    """
    Comprueba si una sublista es la lista máxima dentro de la lista de listas.

    :param sublista: La sublista a verificar.
    :type sublista: list
    :param lista_de_listas: La lista de listas que contiene todas las sublistas.
    :type lista_de_listas: list
    :return: True si la sublista es la máxima, False de lo contrario.
    :rtype: bool
    """
    return sublista == max(lista_de_listas, key=max)

def maximos_por_lista(lista_de_listas):
    """
    Encuentra las sublistas máximas dentro de una lista de listas.

    :param lista_de_listas: La lista de listas que contiene todas las sublistas.
    :type lista_de_listas: list
    :return: Una lista de las sublistas máximas.
    :rtype: list
    """
    pdb.set_trace()  # Punto de parada antes de la comprensión de listas
    return list(filter(lambda sublista: es_maximo(sublista, lista_de_listas), lista_de_listas))
