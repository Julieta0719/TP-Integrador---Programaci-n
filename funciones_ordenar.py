import csv
from funciones_menu import limpiar_consola
from datos_consola import console
#Funcion para ordenar los países alfabéticamente
def ordenar_paises():

    limpiar_consola()

    console.print("[titulo]---Países en orden alfabético---[/titulo]")

    #Abrir el archivo csv en modo lectura
    with open("paises.csv", "r", encoding="utf-8") as archivo:

        lectura = csv.DictReader(archivo)

        #Guardar el diccionario en una lista para poder ordenarlo con la funcion sorted()
        lista_paises = list(lectura)

        #Ordenar los países alfabéticamente
        paises_ordenados = sorted(lista_paises, key=lambda pais: pais["Nombre"].lower())

        #Mostrar los países ordenados
        for pais in paises_ordenados:
            console.print(f"[exito]{pais["Nombre"]}[/exito]")



#Funcion para ordenar poblaciones de menor a mayor
def ordenar_poblacion():
    
    limpiar_consola()

    console.print("[titulo]---Poblaciones de menor a mayor---[/titulo]")

    #Abrir el archivo csv en modo lectura
    with open("paises.csv", "r", encoding="utf-8") as archivo:

        lectura = csv.DictReader(archivo)

        #Guardar el dicc en una lista para ordenar sus poblaciones
        lista_poblaciones = list(lectura)

        #Ordenar las poblaciones de menor a mayor
        poblaciones_ordenadas = sorted(lista_poblaciones, key=lambda poblacion: int(poblacion["Población"]))
        
        #Mostrar las poblaciones ordenadas
        for poblacion in poblaciones_ordenadas:
            console.print(f"[opcion]{poblacion["Nombre"]}[/opcion]  | [opcion]{poblacion["Población"]}[/opcion]")




#Funcion para ordenar superficies de forma ascendente
def ordenar_superficie():

    limpiar_consola()

    console.print("[titulo]---Superficies en orden ascendente---[/titulo]")

    #Abrir el archivo csv en modo lectura
    with open("paises.csv", "r", encoding="utf-8") as archivo:

        lectura = csv.DictReader(archivo)

        #Guardar el dicc en una lista para ordenarlos
        lista_superficies = list(lectura)

        #Ordenar las superficies de manera ascendente
        superficies_ordenadas = sorted(lista_superficies, key=lambda superficie: float(superficie["Superficie"]))
        
        #Mostrar las poblaciones ordenadas
        for superficie in superficies_ordenadas:
            console.print(f"[opcion]{superficie["Nombre"]}[/opcion]   |  [exito]{superficie["Superficie"]}[/exito]")