from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.completion import WordCompleter
from loguru import logger

console = Console()

def mostrar_menu():
    
    console.print(Panel(
    "------------------------------------\n" \
    " [1]: Buscar un país por su nombre\n" \
    " [2]: Filtrar países\n" \
    " [3]: Ordenar países\n" \
    " [4]: Mostrar estadísticas\n"
    " [5]: Salir\n" 
    "------------------------------------",
    title="Menu principal", subtitle="Seleccione una opcion",style="bold cyan"))

def preguntar_opcion():
    
    #Bucle while para consultar el número cuantas veces sea necesario (si se ingresa mal)
    menu_flag: bool = True
    while menu_flag:

        opcion = input("Por favor, ingrese el número de la opción de la que desea interactuar: ")

        if opcion.isdigit() and opcion.strip() != "" and opcion in ["1","2","3","4","5"]:
            opcion = int(opcion)
            #Opción 1
            if opcion == 1:
                pass

            #Opción 2
            elif opcion == 2:
                pass

            #Opción 3
            elif opcion == 3:
                pass

            #Opción 4
            elif opcion == 4:
                pass
                
            #Opción 5
            elif opcion == 5:
                print("Saliendo...")
                menu_flag = False
            else:
                print()
        else:
            print("La opcion debe ser un numero entre 1 y 5")
            menu_flag = True

