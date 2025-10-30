import json


# Seccion : nombres y rutas de archivos: 
CSV_CANCIONES_LADYGAGA = 'C:/Repositorio UTN/2025/PROG I/Practica_Conceptos/10_Archivos_Quest_Lady_gaga/canciones.csv'
CSV_CANCIONES_LADYGAGA_VACIO = 'C:/Repositorio UTN/2025/PROG I/Practica_Conceptos/10_Archivos_Quest_Lady_gaga/canciones_vacio.csv'
JSON_FILE = '../10_Archivos_Quest_Lady_gaga/heroes.json' # testing
JSON_FILE_CANCIONES_LADY_GAGA = '../10_Archivos_Quest_Lady_gaga/canciones.json'


# Quest Lady Gaga  - Seccion : funcionciones basicas  ---------------

def obtener_encabezado(cancion: dict) -> str:
    encabezado = ''
    for key in cancion.keys():
        encabezado += f'{key};'
    encabezado = encabezado[:-1]
    return encabezado

def parsear_dict_a_csv_str(cancion: dict) -> str:
    """ Recorre los valores del diccionario, y los concatena en una lista de strings"""
    info = ''
    for value in cancion.values():
        info = f'{info}{value};'
    # "goku,saiyan,100,50"
    info = info[:-1]
    return info

# Validaciones de archivo / contenido leido 
def es_contenido_vacio(contenido: list, mensaje: str) -> bool:
    
    
    if len(contenido) == 0: 
        mensaje_error= mensaje
        print(mensaje_error)
        contenido_vacio = True
    else: 
        contenido_vacio = False

    return contenido_vacio
        

# Quest Lady Gaga  - Seccion : Apertura y cierre de archivos  ---------------

def abrir_archivo(ruta: str, modo = 'r') -> int:
    """ Abre un archivo que ya existe """
    archivo = open(ruta, mode= modo , encoding='UTF-8')
    return archivo

def cerrar_archivo(archivo):
    """ Cierra un archivo que ya existe """
    return archivo.close() 

def abrir_escribir_texto(ruta: str, contenido: str, anexar: bool = False) -> int:
    """ Abre un archivo (si no existe, lo crea), lo graba y lo cierra """
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

# Quest Lady Gaga  - Crear archivo CSV -------------------

def crear_archivo_csv(playlist_lady_gaga: list[dict]):
    """ Crea un archivo a partir de una lista de diccionarios.
        1 - Arma un encabezado con las claves correspondientes a los valores 
        2 - A partir de la lista de dict cargada en memoria, procesa uno por uno, accediendo
            a la estructura del diccionario
        3 - Dentro del proceso llama a una funcion que realiza parseo de dict a lista de strings (un reg. en linea con todos los valores)
        4 - Llama a funcion para grabar en el archivo, ese registro que tiene cargado en memoria. 
        Procesa hasta fin de lista de diccionarios.    

    :params:
         playlist_lady_gaga -> lista de diccionarios """
    
    encabezado = obtener_encabezado(playlist_lady_gaga[0])
    abrir_escribir_texto(CSV_CANCIONES_LADYGAGA, contenido= encabezado)

    for cancion in playlist_lady_gaga:

        info = parsear_dict_a_csv_str(cancion) 

        info_canciones = ''
        info_canciones += f'\n{info}'
        abrir_escribir_texto(CSV_CANCIONES_LADYGAGA, contenido= info_canciones, anexar=True)


# Quest Lady Gaga  - Seccion : Leer archivo -------------------

def leer_archivo(nombre_archivo):
    """ Lee un archivo con metodo  .read() """
    contenido = nombre_archivo.read()
    return contenido

def leer_archivo_read_lines(nombre_archivo) -> list:
    """ Lee un archivo con metodo .readlines() , y elimina el salto de linea implicito 
        que viene por defecto al levantar
    :params: nombre_archivo -> archivo a leer
    :returns: lista_contenido -> lista con todos los registros del archivo  """
    lista_contenido = []
    lista_contenido = nombre_archivo.readlines()

    for indice_fila in range(len(lista_contenido)):
        lista_contenido[indice_fila] = lista_contenido[indice_fila].replace('\n', '')

    return lista_contenido

def cargar_datos_desde_archivo_lista(nombre_archivo) -> list[str]:
    """ 1 - Lee un archivo y carga su contenido por a una lista de strings
        2 - Valida archivo vacio: Si la lista que carga no està cargada es porque leyò archivo vacìo.
            2.a - Llama a una funcion que devuelve True si la lista està vacia o False si cargò datos.
                Si en la vaidacion el resultado es True -> Mostrara msj de error, no ejecutarà nada y tampoco rompe.
                Si en la vaidacion el resultado es False -> imprimirà por consola lo que cargò desde la lectura.
                
        3 - Elimina el encabezado si es que lo trae pero hay que ajustarlo a mano por el momento (LEER COMENTARIO EN VERDE)
        4 - Cierra el archivo 
        5 - Devuelve la lista
        :params:
            nombre_archivo -> ruta del archivo
        :returns:
            lista_contenidos -> lista de strings
     """
    
    contenido = list()
    archivo = abrir_archivo(nombre_archivo, modo='r')

    contenido = leer_archivo_read_lines(archivo)
    if not es_contenido_vacio(contenido, mensaje= 'Error en func -> leer_imprimir_archivo() -> El archivo està vacìo'):
    
        lista_claves = contenido.pop(0).split(';') # <- OJO ACA QUE ELIMINA EL PRIMER REG PORQUE VIENE CON ENCABEZADO
        lista_contenidos = contenido.split(';')
    else: 
        mensaje_error= 'Error en func -> cargar_datos_desde_archivo() -> El archivo " {nombre_archivo} " està Vacio'
        print(mensaje_error)
    
    archivo.close()
    return lista_contenidos

def crear_diccionario(lista_claves: list, lista_contenido : list[str]) -> dict:
    """ Arma un diccionario con claves y valores obtenidas por parametro y
        devuelve una estructura de datos de tipo dict """
    diccionario = {}
    
    for index_key in range(len(lista_claves)):
        nombre_clave = lista_claves[index_key]
        nombre_valor = lista_contenido[index_key]

        diccionario[nombre_clave] = nombre_valor

    return diccionario
   
def cargar_datos_a_diccionario_desde_archivo(nombre_archivo) -> list[dict]:
    """ 1 - Lee un archivo y carga su contenido por a una lista de strings
        2 - Valida archivo vacio: Si la lista que carga no està cargada es porque leyò archivo vacìo.
            2.a - Llama a una funcion que devuelve True si la lista està vacia o False si cargò datos.
                Si en la vaidacion el resultado es True -> Mostrara msj de error, no ejecutarà nada y tampoco rompe.
                Si en la vaidacion el resultado es False -> imprimirà por consola lo que cargò desde la lectura.
                
        3 - separa el encabezado que contiene las claves si es que lo trae pero hay que ajustarlo a mano por el momento 
            (LEER COMENTARIO EN VERDE)

        4 - PROCESO PRINCIPAL : Por cada elemento en la lista de datos obtenidos desde la lectura del archivo, llama a una funcion que crea un diccionario
            de datos, obtenidos por parametro -> lista de claves y el registro (valores) y anexa ese diccionario.  
        5 - Cierra el archivo 
        5 - Devuelve la lista de diccionarios
        :params:
            nombre_archivo -> ruta del archivo
        :returns:
            contenido -> lista de diccionarios
     """
    
    contenido = []
    diccionario = {}
    lista_diccionarios = []
    archivo = abrir_archivo(nombre_archivo, modo='r')

    contenido = leer_archivo_read_lines(archivo)
    if not es_contenido_vacio(contenido, mensaje= 'Error en func -> leer_imprimir_archivo() -> El archivo està vacìo'):
    
        lista_claves = contenido.pop(0) # <- OJO ACA QUE ELIMINA EL PRIMER REG PORQUE VIENE CON ENCABEZADO
        nombres_claves = lista_claves.split(';') # separo los campos
        for reg in contenido:
      
            valores_registro = reg.split(';') # separo los campos
            diccionario = crear_diccionario(lista_claves= nombres_claves, lista_contenido= valores_registro)
            
            lista_diccionarios.append(diccionario)   
    else: 
        mensaje_error= 'Error en func -> cargar_datos_desde_archivo() -> El archivo " {nombre_archivo} " està Vacio'
        print(mensaje_error)
    
    archivo.close()
    return lista_diccionarios
    
# Quest Lady Gaga  - Seccion : JSON file  -------------------


def abrir_grabar_archivo_json(nombre_archivo: str, modo: str, contenido: list[dict], clave: str, anexo: bool = False):
    modo = 'w'
    if anexo == True:
        modo = 'a'

    with open(nombre_archivo, modo, encoding='UTF-8') as file:

        diccionario = {}
        diccionario[clave] = contenido # <- creo una clave para almacenar una lista de datos y la agrego en el paso siguiente.
        json.dump(diccionario, file, indent=4) # <- le paso que quiero guradar (datos) y donde (file) | indent=4 <- acomoda verticalmente la informacion






# TESTING -------------------------------------------------------------------------------------| 
#if __name__ == '__main__':
   

    
#    cargar_datos_desde_archivo(CSV_CANCIONES_LADYGAGA_VACIO)
#    cargar_datos_desde_archivo_lista(CSV_CANCIONES_LADYGAGA)

#    lista_diccionarios = cargar_datos_a_diccionario_desde_archivo(CSV_CANCIONES_LADYGAGA)
#    cantidad_impresos = 0
#    for diccionario in lista_diccionarios:
#        for clave, valor in diccionario.items():
#            print(f'{clave} : {valor}')
#        print()
#        cantidad_impresos += 1
#    print('-----------------------------------------------------------------------------------')
#    print(f'Total impresos: {cantidad_impresos}')
#    print('-----------------------------------------------------------------------------------\n\n')