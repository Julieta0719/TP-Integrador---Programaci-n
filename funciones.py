import requests
import csv
import json

def obtener_datos(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()

        datos = respuesta.json()
        return datos

    except requests.exceptions.RequestException as e:
        print(f" Error al conectar con la API: {e}")
        return []

    except json.JSONDecodeError:
        print("Error al convertir la respuesta a JSON.")
        return []
    
def validar_datos(paises):
    paises_validos = []

    for pais in paises:
        try:
            nombre = pais["name"]["common"]
            poblacion = pais.get("population", None)
            superficie = pais.get("area", None)
            continente = pais["continents"][0]

            if not nombre or not isinstance(poblacion, (int, float)) or not isinstance(superficie, (int, float)):
                continue

            paises_validos.append({
                "nombre": nombre,
                "poblacion": poblacion,
                "superficie": superficie,
                "continente": continente
            })

        except (KeyError, IndexError, TypeError):
            continue

    return paises_validos

def formatear_datos(paises):
    encabezado = ["Nombre", "Población", "Superficie", "Continente"]
    filas = [encabezado]

    for pais in paises:
        fila = [
            pais["nombre"],
            pais["poblacion"],
            pais["superficie"],
            pais["continente"]
        ]
        filas.append(fila)

    return filas

def guardar_en_csv(nombre_archivo, datos):
    try:
        with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(datos)
        print(f"Archivo '{nombre_archivo}' guardado correctamente.")

    except IOError as e:
        print(f"Error al escribir el archivo CSV: {e}")

def main():
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