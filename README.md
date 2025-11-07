# TP-Integrador---Programaci-n
Trabajo Práctico Integrador de Programación I
Comisión: 1prog2, TT - Integrantes: Matias Ezequiel Maigua, Julieta Cáceres Characán

--Intrucciones de uso--
Clonado del repositorio:
Copiar la url del repositorio y abrir VSC, iniciar una nueva terminal y colocar el comando "git clone <url>"

Ejecutar el programa en Docker:
Primero se debe abrir el Docker Desktop, luego abrir una terminal en VSC y creamos la imágen que utilizaremos para el contenedor con el comando "docker build -t nombre_imagen", una vez que se haya finalizado
la creación de la imágen creamos e iniciamos el contenedor usando el comando "docker run -it --rm --name nombre_contenedor nombre_imagen" y automáticamente estaremos ejecutando el programa con Docker.

Ejecución:
Una vez iniciado el programa veremos un mensaje que comunicará si el archivo CSV existe, en el caso de que no exista se va a crear, y sino se omite su creación. También se verá un mensaje de bienvenida.

En el menú principal se mostraran las opciones con las que puede interactuar y se le pedira ingresar el número de la opción.
-OPCION 1:
Si elige la opción 1 se le pedirá ingresar el nombre de un país para buscar y mostrar por consola sus respectiva información como nombre, población, superficie y continente. El programa contiene funciones para
hacer tanto una busqueda exacta (es decir que se ingrese el nombre exactamente igual que se encuentra en el archivo CSV) o de manera parcial (Muestra todos los países que coincidan con la palabra ingresada)
Una vez finalizada la busqueda, se va a pedir que se ingrese la tecla enter para volver al menú principal.

-OPCION 2:
Si elige la opción 2 se le mostrará un menú con 3 opciones para elegir.

Opcion 1 (Filtrar países por continente): Se le mostrará otro menú con 5 continentes (Africa, America, Asia, Europa y Oceania) y debera ingresar un número del 1 al 5 para ver los países que pertenecen a ese continente y luego se le mostrara el MENÚ DE RETORNO: "Que desea hacer ahora" y debera ingresar (1: para volver al menú anterior, 2: Para continuar en el menú actual).

Opción 2 (Filtrar países por rango de población): Se le pedirá ingresar un rango mínimo y máximo y se le mostrarán todos los países que tengan una población dentro del rango ingresado. Nuevamente vera el menú de retorno para volver al menú principal o para continuar en el actual.

Opción 3 (Filtar países por rango de Superficie): Muy parecido a la opción anterior, se le pedirá ingresar un rango mínimo y máximo y vera los países que tengan una superficie dentro de ese rango, y luego vera el menú de retorno.

-OPCION 3:
Se le mostrara un menú con las 3 siguientes opciones para elegir
Opcion 1 (Ordenar países alfabeticamente): Se le mostrara por consola todos los nombres de los países ordenados de manera alfabetica y luego vera el menu de retorno

Opcion 2 (Ordenar población de menor a mayor): Se le mostraran todos los nombres y poblaciones ordenados de menor a mayor y vera el menu de retorno

Opcion 3 (Ordenar superficie de forma ascendente): Se le mostraran los nombres y superficies ordenados de manera ascendente, y se vera el menu de retorno

-OPCION 4:
Se le mostrara un menu con 4 opciones:
Luego de seleccionar cada una de las opciones vera el menu de retorno

Opcion 1 (País con menor y mayor población): Se le mostrara el nombre y población del país con menor y mayor población del archivo CSV

Opcion 2 (Promedio de las poblaciones): Se mostrara el promedio obtenido de la suma de todas las poblaciones dividido la cantidad de las mismas

Opcion 3 (Promedio de las superficies): Lo mismo que la opción anterior pero se mostrara el promedio obtenido de las superficies

Opcion 4 (Cantidad de países por continente): Se le mostrara el nombre de cada continente (Africa, America, Asia, Europa y Oceanía) y seguido de dos puntos se vera el número de países que contiene el continente

-OPCION 5:
Se le mostrara un mensaje que diga "---Gracias por usar el programa!---" y finalizará la ejecución del programa.


--Ejemplos de entradas y salidas--
.

--Participación de los integrantes--
Matias Ezequiel Maigua: Implementación de los archivos "main", "funciones", "dockerfile", "requirements.txt" "datos_consola", llamado de la API, validación de los datos obtenidos de la API, formateo de datos, cración y validación de existencia del archivo CSV con los datos de los países, importación de librerias y decorado de la consola, creación, importación y llamado del menú de retorno y mensaje de bienvenida

Julieta Cáceres Characán: Implementación de los archivos "funciones_menu", "funciones_validaciones", "funciones_filtrar", "funciones_ordenar", "funciones_estadisticas", Creación de la estructura y funciones del menú principal, y de los submenus de cada opcion. Importaciones y llamados a las funciones que realizan cada tarea específica, validaciones para evitar que el programa se rompa y finalice solo cuando el usuario elija la opción 5, validar datos ingresados y dar mensajes de éxito o de error.
