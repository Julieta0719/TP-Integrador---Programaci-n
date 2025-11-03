import csv
from funciones_menu import limpiar_consola
from datos_consola import console
from rich.table import Table
from rich.console import Console
console = Console()

#--------------------------------------------------------------------------------------------------------------------------

#Funcion para ordenar los países alfabéticamente (Opcion 1 del menú de ordenamiento)
def ordenar_paises():

    limpiar_consola()

    

    #Abrir el archivo csv en modo lectura
    with open("paises.csv", "r", encoding="utf-8") as archivo:

        lectura = csv.DictReader(archivo)

        #Guardar el diccionario en una lista para poder ordenarlo con la funcion sorted()
        lista_paises = list(lectura)

        #Ordenar los países alfabéticamente
        paises_ordenados = sorted(lista_paises, key=lambda pais: pais["Nombre"].lower())

        tabla = Table(title="[bold yellow]-----Países en orden alfabético-----[/bold yellow]",style="bold yellow")
        tabla.add_column("[bold cyan]Pais[/bold cyan]", style="bold cyan")

        #Mostrar los países ordenados
        for pais in paises_ordenados:
            tabla.add_row(f"{pais['Nombre']}",style="bold green")
        console.print(tabla)

#--------------------------------------------------------------------------------------------------------------------------

#Funcion para ordenar poblaciones de menor a mayor (Opción 2 del menú de ordenamiento)
def ordenar_poblacion():
    
    limpiar_consola()

    #Abrir el archivo csv en modo lectura
    with open("paises.csv", "r", encoding="utf-8") as archivo:

        lectura = csv.DictReader(archivo)

        #Guardar el dicc en una lista para ordenar sus poblaciones
        lista_poblaciones = list(lectura)

        #Ordenar las poblaciones de menor a mayor
        poblaciones_ordenadas = sorted(lista_poblaciones, key=lambda poblacion: int(poblacion["Población"]))
        
        tabla = Table(title= "[bold yellow]-----Poblaciones de menor a mayor-----[/bold yellow]", style="bold yellow")
        tabla.add_column("[bold cyan]Pais[/bold cyan]", style="bold cyan")
        tabla.add_column("[bold blue]Poblacion[/bold blue]", style="bold blue")

        #Mostrar las poblaciones ordenadas
        for poblacion in poblaciones_ordenadas:
            tabla.add_row(f"[opcion]{poblacion['Nombre']}[/opcion] -->", f"[opcion]{poblacion['Población']}[/opcion]")
        console.print(tabla)


#--------------------------------------------------------------------------------------------------------------------------

#Funcion para ordenar superficies de forma ascendente (Opcion 3 del menú de ordenamiento)
def ordenar_superficie():

    limpiar_consola()

    

    #Abrir el archivo csv en modo lectura
    with open("paises.csv", "r", encoding="utf-8") as archivo:

        lectura = csv.DictReader(archivo)

        #Guardar el dicc en una lista para ordenarlos
        lista_superficies = list(lectura)

        #Ordenar las superficies de manera ascendente
        superficies_ordenadas = sorted(lista_superficies, key=lambda superficie: float(superficie["Superficie"]))
        
        tabla = Table(title= "[bold yellow]-----Superficies en orden ascendente-----[/bold yellow]", style="bold yellow")
        tabla.add_column("[bold cyan]Pais[/bold cyan]", style="bold cyan")
        tabla.add_column("[bold blue]Superficie[/bold blue]", style="bold blue")
        #Mostrar las poblaciones ordenadas
        for superficie in superficies_ordenadas:
            tabla.add_row(f"[opcion]{superficie['Nombre']}[/opcion] -->", f"[exito]{superficie['Superficie']} km²[/exito]")
        console.print(tabla)