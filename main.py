import os
from funciones import obtener_datos, validar_datos, formatear_datos, guardar_en_csv
def main():
    datos_pais = "paises.csv"

    # Verificamos si el CSV ya existe
    if os.path.exists(datos_pais):
        print(f"El archivo '{datos_pais}' ya existe.")
        print("Se omite la descarga desde la API.")
        return 
    url = "https://restcountries.com/v3.1/all?fields=name,area,continents,population,translations"
    datos_api = obtener_datos(url)

    if not datos_api:
        print("No se pudieron obtener datos de la API.")
        return

    paises_validos = validar_datos(datos_api)
    datos_formateados = formatear_datos(paises_validos)
    guardar_en_csv("paises.csv", datos_formateados)
if __name__ == "__main__":
    main()


#Importación y llamado de funciones del menú
from funciones_menu import mostrar_menu, preguntar_opcion
mostrar_menu()

preguntar_opcion()