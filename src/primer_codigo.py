from gettext import install
from ast import parse
from operator import truediv
import numpy as np
import argparse

def calcular_min_max(lista_numeros, verbose=1):
    #Retorna los valores minimo y maximo de una lista de numeros
    #Argumentos: 
    #lista_numeros: type list

    min_value = min(lista_numeros)
    max_value = max(lista_numeros)

    if verbose == 1:
        print("Valor minimo:",min_value)
        print("Valor maximo:",max_value)
    else:
        pass
    return min_value, max_value

#Calcular la media y la Desviación Estandar:

def calcular_valores_centrales(lista_numeros, verbose=1):
    """Calcula la media y la desviación estandar de una lista de numeros

    Args:
        lista_numeros (list): lista con valores numericos
        verbose (bool, optional): Para decidir si imprimir mensajes en pantalla. Defaults to True.

    Returns:
        tuple: (media, dev_std)
    """
    media = np.mean(lista_numeros)
    dev_std = np.std(lista_numeros)
    if verbose == 1:
        print("Media:",media)
        print("Desviación Estandar:",dev_std)
    else:
        pass
    return media, dev_std

#calcular_valores = (lista_Valores, verbose=True)


def calcular_suma(lista_numeros, verbose=1):
    
    suma = np.sum(lista_numeros) #Calcular_suma(lista_numeros)
    #min_val, max_val = calcular_min_max(lista_numeros, verbose)
    #media, dev_std = calcular_valores_centrales(lista_numeros)
    return suma

lista_Valores = [5,4,8,9,21]

test = calcular_min_max(lista_Valores, verbose=1)
test2 = calcular_valores_centrales(lista_Valores, verbose=1)
test3 = calcular_suma(lista_Valores, verbose=1)
print(test, test2, test3)

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("--verbose", type=int, default=1, help="Para imprimir en pantalla información")
    args = parser.parse_args()

    lista_Valores = [5,4,8,9,21]
    calcular_valores(lista_numeros=lista_Valores, verbose=args.verbose)
    
if __name__== "main":
    main()
