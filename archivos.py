from lady_gaga import playlist_lady_gaga

# Quest Lady Gaga  - funcionciones basicas  ---------------
def abrir_escribir_texto(ruta: str, contenido: str, anexar: bool = False) -> int:
    lineas = 0
#    modo = 'w'
    modo = 'w+'
    if anexar == True:
        modo = 'a'

    with open(ruta, modo, encoding='utf-8') as file:
        lineas = file.write(contenido)
    
    if lineas > 0:
        return file
    else:
        return -1

def obtener_encabezado(cancion: dict) -> str:
    encabezado = ''
    for key in cancion.keys():
        encabezado += f'{key};'
    encabezado = encabezado[:-1]
    return encabezado

def parsear_dict_a_csv_str(cancion: dict) -> str:
    info = ''
    for value in cancion.values():
        info = f'{info}{value};'
    # "goku,saiyan,100,50"
    info = info[:-1]
    return info

# Quest Lady Gaga  - Crear archivo CSV -------------------

CSV_CANCIONES_LADYGAGA = 'C:/Repositorio UTN/2025/PROG I/Practica_Conceptos/10_Archivos_Quest_Lady_gaga/canciones.csv'

def crear_archivo_csv(playlist_lady_gaga: list[dict]):
    """ Crea un archivo a partir de una lista de diccionarios 
    :params:
         playlist_lady_gaga -> lista de diccionarios """
    
    encabezado = obtener_encabezado(playlist_lady_gaga[0])
    abrir_escribir_texto(CSV_CANCIONES_LADYGAGA, contenido= encabezado)

    for cancion in playlist_lady_gaga:

        info = parsear_dict_a_csv_str(cancion) 

        info_canciones = ''
        info_canciones += f'\n{info}'
        abrir_escribir_texto(CSV_CANCIONES_LADYGAGA, contenido= info_canciones, anexar=True)


