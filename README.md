�
�
 Análisis de Lista de Reproducción - Lady Gaga (Uso de Archivos CSV y JSON) 
Disponemos de información sobre una lista de reproducción de la cantante Lady Gaga, 
almacenada en un archivo CSV. Nuestro objetivo es desarrollar funciones para leer, 
procesar y analizar estos datos, normalizándolos y permitiendo distintas consultas sobre 
la lista de reproducción. 
�
�
 Manejo de Archivos 
✅📥
 Obtener Datos CSV: 
● Leer los datos de un archivo llamado canciones.csv y cargarlos en una 
estructura manipulable en Python. 
✅📤
 Guardar en JSON: 
● Guardar en un archivo JSON todas las canciones luego de ser normalizadas. 
✅📤
 Guardar en CSV: 
● Guardar en un archivo colaboradores.csv la lista de canciones que incluyan un 
colaborador específico. 
�
�
 Funcionalidades del Software 
�
�
 1. Normalización de Datos 
El formato original de los datos no está estandarizado, por lo que se deben normalizar 
utilizando funciones preexistentes. Cada video deberá contener la siguiente información 
correctamente estructurada: 
● Título (str): Nombre del tema. 
● Colaboradores (list): Lista de artistas invitados (si los hay). 
● Vistas (int): Cantidad de reproducciones en números enteros. 
● Duración (int): Duración del video en segundos. 
● Link (str): Enlace directo al video en YouTube. 
● Fecha de lanzamiento (date): Fecha de publicación del video. 
�
�
 2. Mostrar Lista de Temas 
Se presentará la lista de todos los temas en formato tabular. No es necesario mostrar 
todos los datos, solo los esenciales (por ejemplo, título y duración). 
�
�
 3. Ordenar Temas 
Los videos se ordenarán por duración, de mayor a menor. 
2 
Programación I 
Scarafilo Germán - Gatto Catriel - Ochoa Gonzalo 
Guía Archivos 
�
�
 4. Promedio de Vistas 
Se calculará y mostrará el promedio de vistas de todos los videos en millones. 
�
�
 5. Máxima Reproducción 
Se listará el video (o los videos) con la mayor cantidad de vistas. 
�
�
 6. Mínima Reproducción 
Se listará el video (o los videos) con la menor cantidad de vistas. 
�
�
 7. Búsqueda por Código 
El usuario ingresará un código de video y el programa mostrará todos los detalles 
asociados a ese video. 
�
�
 8. Listar por Colaborador 
● El usuario ingresará el nombre de un colaborador (de una lista de colaboradores 
existentes) y el programa mostrará todos los videos en los que haya participado. 
● Estos datos se guardarán en colaboradores.csv. 
�
�
 9. Listar por Mes de Lanzamiento 
El usuario ingresará un mes y se listarán todos los temas lanzados en ese mes, sin 
importar el año. 
�
�
 10. Guardar en JSON: 
● Luego de normalizar los datos, se guardará toda la información en un archivo 
JSON. 
�
�
 11. Salir 
Finalizar la ejecución del programa. 
�
�
 Requisitos del Desarrollo 
✅
 Estructura Modular: Separar las funcionalidades en funciones específicas. 
✅
 Uso de Tipado: Implementar anotaciones de tipo en las funciones. 
✅
 Validaciones: Manejar posibles errores en la lectura del archivo y los formatos de 
datos. 
✅
 Optimización: Implementar soluciones claras y eficientes. 
�
�
 Objetivo Final 
Este programa permitirá automatizar el análisis de una lista de reproducción de Lady 
Gaga, facilitando su consulta y almacenamiento en diferentes formatos.
