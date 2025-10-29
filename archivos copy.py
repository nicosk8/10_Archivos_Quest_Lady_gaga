from lady_gaga import playlist_lady_gaga


def abrir_escribir_texto(ruta: str, contenido: str, anexar: bool = False) -> int:
    lineas = 0
#   modo = 'w'
    modo = 'w+'
    if anexar == True:
        modo = 'a'

    with open(ruta, modo, encoding='utf-8') as file:
        lineas = file.write(contenido)
    return lineas

def obtener_encabezado(cancion: dict) -> str:
    encabezado = ''
    for key in cancion.keys():
        encabezado += f'{key},'
    encabezado = encabezado[:-1]
    return encabezado

def parsear_dict_a_csv_str(cancion: dict) -> str:
    info = ''
    for value in cancion.values():
        info = f'{info}{value},'
    # "goku,saiyan,100,50"
    info = info[:-1]
    return info


# una vez que tengo mi encabezado, deberia ir a grabar archivo.
def grabar_archivo(file: any, contenido: str):
    
    lineas = file.write(contenido)


def armar_encabezado():
    info_canciones = obtener_encabezado(playlist_lady_gaga[0])
    grabar_archivo()
#--------------------------
for cancion in playlist_lady_gaga:
    info = parsear_dict_a_csv_str(cancion) 

    info_canciones += f'\n{info}'


CSV_CANCIONES_LADYGAGA = 'C:/Repositorio UTN/2025/PROG I/Practica_Conceptos/10_Archivos_Quest_Lady_gaga/Lady_gaga_songs.csv'
#abrir_escribir_texto(CSV_CANCIONES_LADYGAGA, info_canciones)


def open_file(ruta_archivo: str, modo: str = 'r+'):
    """  Abre un archivo y lo retorna """
    file = open(ruta_archivo, mode= modo)
    return file

def abrir_archivo(ruta_archivo: str, modo: str):

    """ Rutina de apertura de archivo. Valida file status. """

    ARCHIVO = open_file(ruta_archivo, modo='r')
    if not ARCHIVO == __file__:
        # // rutina manejo de errores - cancelacion 
        ERROR_MSG = 'Error en apertura de archivo: {CSV_CANCIONES_LADYGAGA} . Modo de apertura : {modo} - File status -> {ARCHIVO}' # ver duda por file status
        print(ERROR_MSG)
        return -1
    return ARCHIVO

ENTRADA = abrir_archivo(CSV_CANCIONES_LADYGAGA, modo='r+')
armar_encabezado()
