import csv

from funciones_menu import limpiar_consola

def buscar_mayor_poblacion():

    limpiar_consola()

    #Abrir el archivo en modo de lectura
    with open("paises.csv", "r", encoding="utf-8") as archivo:

        lectura = csv.DictReader(archivo)

        paises = list(lectura)

        #Buscar la mayor cantidad de población
        mayor_poblacion = max(paises, key=lambda poblacion: int(poblacion["Población"]))

        print("---País con mayor población---")
        print(mayor_poblacion["Nombre"], mayor_poblacion["Población"])


def buscar_menor_poblacion():

    limpiar_consola()

    #Abrir archivo en modo de lectura
    with open("paises.csv", "r", encoding="utf-8") as archivo:

        lectura = csv.DictReader(archivo)

        paises = list(lectura)

        #Buscar la menor cantidad de población
        menor_poblacion = min(paises, key=lambda poblacion: int(poblacion["Población"]))

        print("---País con menor población---")
        print(menor_poblacion['Nombre'], menor_poblacion['Población'])


def promedio_poblaciones():
    
    limpiar_consola()

    #Abrir el archivo en lectura
    with open("paises.csv", "r", encoding="utf-8") as archivo:
        lectura = csv.DictReader(archivo)

        #Se lee linea por linea
        for linea in lectura:
            
            #Convertir a flotante el dato en la linea actual y asignarlo a una variable
            poblacion = float(linea["Población"])
            
            #Sumar la población
            suma_poblacion = 0
            suma_poblacion = suma_poblacion + poblacion

            #Sacar el promedio
            promedio_poblacion = suma_poblacion //250

    print("---Promedio de la población---")
    print(promedio_poblacion)


def promedio_superficies():
    
    limpiar_consola()

    #Abrir el archivo en lectura
    with open("paises.csv", "r", encoding="utf-8") as archivo:
        lectura = csv.DictReader(archivo)

        #Se lee linea por linea
        for linea in lectura:
            
            #Convertir a flotante el dato en la linea actual y asignarlo a una variable
            superficie = float(linea["Superficie"])
            
            #Sumar la población
            suma_superficie = 0
            suma_superficie = suma_superficie + superficie

            #Sacar el promedio
            promedio_superficie = suma_superficie //250

    print("---Promedio de la superficie---")
    print(promedio_superficie)
    


def contar_pais_por_continente():
    
    limpiar_consola()

    contador = {}
    with open("paises.csv", "r", encoding="utf-8") as archivo:

        lector = csv.DictReader(archivo)

        for pais in lector:
            continente = pais.get("Continente","").strip()
            if continente:
                if continente not in contador:
                    contador[continente] = 1
                else:
                    contador[continente] += 1
        print("---Continentes y sus paises---")
        for continente, cantidad in contador.items():
            print(f"--{continente}: {cantidad} paises")