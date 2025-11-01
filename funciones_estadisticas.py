import csv
from datos_consola import console
from funciones_menu import limpiar_consola

#--------------------------------------------------------------------------------------------------------------------------
#Funcion para encontrar el pais con mayor numero de población (Opcion 1 del menú de estadísticas)
def buscar_mayor_poblacion():

    #Abrir el archivo en modo de lectura
    with open("paises.csv", "r", encoding="utf-8") as archivo:

        lectura = csv.DictReader(archivo)

        paises = list(lectura)

        #Buscar la mayor cantidad de población
        mayor_poblacion = max(paises, key=lambda poblacion: int(poblacion["Población"]))

        console.print("[titulo]---País con mayor población---[/titulo]")
        console.print(f"[opcion]{mayor_poblacion['Nombre']}[/opcion], [exito]{mayor_poblacion['Población']}[/exito]")
        print(" ")

#--------------------------------------------------------------------------------------------------------------------------
#Funcion para encontrar el país con el menor número de población (Opcion 1 del menú de estadísticas)
def buscar_menor_poblacion():

    #Abrir archivo en modo de lectura
    with open("paises.csv", "r", encoding="utf-8") as archivo:

        lectura = csv.DictReader(archivo)

        paises = list(lectura)

        #Buscar la menor cantidad de población
        menor_poblacion = min(paises, key=lambda poblacion: int(poblacion["Población"]))

        console.print("[titulo]---País con menor población---[/titulo]")
        console.print(f"[opcion]{menor_poblacion['Nombre']}[/opcion], [exito]{menor_poblacion['Población']}[/exito]")
        print(" ")

#--------------------------------------------------------------------------------------------------------------------------

#Funcion para sacar el promedio de las poblaciones de todos los paises (Opción 2 de l menú de estadísticas)
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

    console.print("[titulo]---Promedio de la población---[/titulo]")
    console.print(f"[exito]{promedio_poblacion}[/exito]")

#--------------------------------------------------------------------------------------------------------------------------

#Funcion para sacar el promedio de las superficies de todos los paises (Opcion 3 del menú de estadísticas)
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

    console.print("[titulo]---Promedio de la superficie---[/titulo]")
    console.print(f"[exito]{promedio_superficie}[/exito]")
    
#--------------------------------------------------------------------------------------------------------------------------

#Funcion para contar cuantos países hay en cada continente (Opcion 4 del menú de estadísticas)
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
        console.print("[titulo]---Continentes y sus paises---[/titulo]")
        for continente, cantidad in contador.items():
            console.print(f"[exito]--{continente}: {cantidad} paises[/exito]")