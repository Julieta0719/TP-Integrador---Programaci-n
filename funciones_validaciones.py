import csv
from datos_consola import console
from rich.table import Table
from rich.console import Console
console = Console()

#--------------------------------------------------------------------------------------------------------------------------

#Validación de que la variable contenga un string
def validar_pais(pais_buscado):

    #Eliminar espacios y validar que sea string
    if str(pais_buscado).replace(" ","").isalpha():
        return True
    else:
        console.print("[advertencia]Incorrecto, debe ingresar el nombre de un país[/advertencia]")
        return False

#--------------------------------------------------------------------------------------------------------------------------

#Validación de busqueda de país exacta
def validacion_exacta(pais_buscado):

    #Bandera para evitar que la validacion exacta y parcial impriman dos veces lo mismo
    pais_encontrado_flag: bool = False

    #Se abre el archivo csv para lectura
    with open("paises.csv", "r", newline="", encoding="utf-8") as archivo:
        lectura = csv.DictReader(archivo)

        #Bucle para leer linea por linea
        for linea in lectura:

            #Si el país buscado se encuentra en el archivo csv, se imprime su respectiva información
            if pais_buscado == linea["Nombre"]:
                console.print(f"""[titulo]Nombre: {linea["Nombre"]}[/titulo]
                        [info]Población: {linea["Población"]}[/info]
                        [exito]Superficie: {linea["Superficie"]}[/exito]
                        [opcion]Continente: {linea["Continente"]}[/opcion]""")

                #Verdadero si se encontro el pais en la validacion exacta
                pais_encontrado_flag = True
                break

    return pais_encontrado_flag

#--------------------------------------------------------------------------------------------------------------------------

#Validacion de busqueda de país de forma parcial
def validacion_parcial(pais_buscado):

    #Bandera para evitar imprimir dos veces lo mismo
    pais_encontrado_flag: bool = False

    #Se abre el archivo csv para lectura
    with open("paises.csv", "r", newline="", encoding="utf-8") as archivo:
        lectura = csv.DictReader(archivo)
        tabla = Table(title= "[bold yellow]-----Datos Pais-----[/bold yellow]", style="bold yellow")
        tabla.add_column("[bold cyan]Pais[/bold cyan]", style="bold cyan")
        tabla.add_column("[bold green]Poblacion[/bold green]", style="bold green")
        tabla.add_column("[bold blue]Superficie[/bold blue]", style="bold blue")
        tabla.add_column("[bold white]Continente[/bold white]",style="bold white")
        #Bucle for para leer cada linea del archivo
        for linea in lectura:
            
            #Asignar a una variable el dato de la linea actual
            paises = linea["Nombre"]

            #Si el string ingresado esta en el nombre del pais se muestran sus datos
            if pais_buscado in paises:
                tabla.add_row(f"[titulo]{linea['Nombre']}[/titulo]",
                        f"[info]{linea['Población']}[/info]",
                        f"[exito]{linea['Superficie']}[/exito]",
                        f"[opcion]{linea['Continente']} km²[/opcion]")
                
                #Verdadero si se encontraron coincidencias
                pais_encontrado_flag = True
        console.print(tabla)
        #Condicional para avisar que no se encontraron coincidencias
    if not pais_encontrado_flag:
            console.print(f"[advertencia]El nombre {pais_buscado} no se encontro en el archivo[/advertencia]")
            print(" ")

    return pais_encontrado_flag


