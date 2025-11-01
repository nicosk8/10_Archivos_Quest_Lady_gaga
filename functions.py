import datetime
from archivos import abrir_escribir_texto
# Quest Lady gaga - Normalizar datos ---------------------------------------------------------

def normalizar_nombre_colaborador(video: dict) -> str:
    nombre_tema_base: str = video.get('Tema')
    
    elementos_titulo = nombre_tema_base.split(' - ')
    
    titulo_saneado = ''
    colaboradores = 'No Tiene'

    if len(elementos_titulo) > 1:
        titulo_saneado = elementos_titulo[1]
        colaboradores = elementos_titulo[0]
    else:
        titulo_saneado = elementos_titulo[0]
    video['Tema'] = titulo_saneado
    video['Colaboradores'] = colaboradores # <- inserto un nuevo tipo de dato y le asigno un valor

def normalizar_vistas(video: dict):
    
    datos_vistas = video.get('Vistas').split(' ')
    cantidad = int(datos_vistas[0])
    cantidad_saneada = cantidad * 1000000
    video['Vistas'] = cantidad_saneada

def normalizar_duracion(video: dict):
    
    datos_tiempo = video.get('Duracion').split(':')
    minutos = int(datos_tiempo[0])
    segundos = int(datos_tiempo[1])
    segundos_totales = minutos * 60 + segundos
    video['Duracion'] = segundos_totales

def normalizar_tiempo(video: dict):
    fecha = datetime.datetime.strptime(video.get('Fecha lanzamiento'), '%Y-%m-%d')
    fecha = fecha.date()
    video['Fecha lanzamiento'] = fecha

def normalizar_video(video: dict):

    normalizar_nombre_colaborador(video)
    normalizar_vistas(video)
    normalizar_duracion(video)
    normalizar_tiempo(video)
    video['Link'] = video.get('Link Youtube')

def normalizar_datos(videos: list[dict]) -> list[dict]:
    list_copy = videos.copy()

    for video in list_copy:
        normalizar_video(video)
    return list_copy

# Quest Lady gaga - Imprimir datos ---------------------------------------------------------

def max_caracteres(videos: list[dict], valor: str) -> int:
    cantidad = 0
    for video in videos:
        cadena = str(video.get(valor))
        if len(cadena) > cantidad:
            cantidad = len(cadena)

    return cantidad

def mostrar_info_completa_video(caracteres: int, video: dict):

    colaboradores_normalizados = video.get('Colaboradores').replace('|', '-')
    if len(colaboradores_normalizados) > 15:
        colab_truncado = f'{colaboradores_normalizados[:12]}...'
    else:
        colab_truncado = colaboradores_normalizados
    datos = f'{video.get("Tema"):{caracteres}} | {colab_truncado:15} | {video.get("Duracion"):03} | {video.get('Vistas'):010}'
    print(datos)

# Quest Lady gaga - Armar encabezados -----------------------------------------------------

def calcular_tabulacion(videos: list[dict]) -> tuple: 
    max_char_tema = max_caracteres(videos, valor='Tema')
    max_char_vistas = max_caracteres(videos, valor='Vistas')
    max_char_durac = max_caracteres(videos, valor='Duracion')
    max_char_date = max_caracteres(videos, valor='Fecha lanzamiento')
    max_char_colab = max_caracteres(videos, valor='Colaboradores')
    tabulaciones = max_char_tema, max_char_vistas, max_char_durac, max_char_date, max_char_colab
#    return max_char_tema, max_char_vistas, max_char_durac, max_char_date, max_char_colab
    return tuple(tabulaciones)

def armar_encabezado(texto: str , videos: list[dict]):
    cantidad = 135
    linea = f'{'-' * cantidad} \n'
    tabulacion = ' ' * 50
    titulo_1 = f'{tabulacion}Lista de videos de artista: Lady Gaga \n'
    titulo_2 = f'{texto} \n' 

    max_char_tema, max_char_vistas, max_char_durac, max_char_date, max_char_colab = calcular_tabulacion(videos)
    
    sub_titulos = (f'{"| Tema" :{max_char_tema}} | {"Vistas":{max_char_vistas}} | {"Duracion":{max_char_durac}} | {"Fecha lanzamiento":{max_char_date}}  | {"Colaboradores":{max_char_colab}} \n')
    encabezado = f'{linea}{titulo_1}{linea}{titulo_2}{linea}{sub_titulos}{linea}'
    print(encabezado)

def armar_encabezado_titulo_duracion(texto: str , videos: list[dict]):
    cantidad = 135
    linea = f'{'-' * cantidad} \n'
    tabulacion = ' ' * 50
    titulo_1 = f'{tabulacion}Lista de videos de artista: Lady Gaga \n'
    titulo_2 = f'{texto} \n' 

    max_char_tema, max_char_vistas, max_char_durac, max_char_date, max_char_colab = calcular_tabulacion(videos)
    
    sub_titulos = f'{"| Tema" :{max_char_tema}} |  {"Duracion":{max_char_durac}} \n' 
    encabezado = f'{linea}{titulo_1}{linea}{titulo_2}{linea}{sub_titulos}{linea}'
    print(encabezado)

def armar_encabezado_informe_siete(texto):
    cantidad = 135
    linea = f'{'-' * cantidad} \n'
    titulo = f'{texto} \n'
    sub_titulos = (f'{"| Tema" :15} | {"Colaboradores"} | {"Duracion"} | {"Vistas"} \n')
    encabezado = f'{linea}{titulo}{linea}{sub_titulos}{linea}'
    print(encabezado)

def armar_footer(texto: str):
    cantidad = 135
    linea = f'{'-' * cantidad} \n'
    titulo = f'{texto} \n' 
    footer = f'{linea}{titulo}{linea}'
    print(footer)

# Quest Lady gaga - Imprimir datos   ------------------------------------------------------

def mostrar_videos_completos(videos: list[dict]):
    """ Muestra la informacion completa de los datos de la lista de videos formateados
    :params: videos -> lista de tipo diccionario de datos
    :returns: None"""
    
    max_char_tema, max_char_vistas, max_char_durac, max_char_date, max_char_colabs = calcular_tabulacion(videos)    
    for video in videos: 
        
        tema = video.get("Tema")
        vistas = video.get("Vistas")
        duracion = video.get("Duracion")
        fecha = video.get("Fecha lanzamiento")
        colabs = video.get("Colaboradores").replace('|', '-')
    
        datos = f'{tema:{max_char_tema}} | {vistas:{max_char_vistas}} | {duracion:{max_char_durac + 5}} |     {str(fecha):{max_char_date}}     | {colabs:{max_char_colabs}}'
        print(datos)
    
def mostrar_videos_completos_titulo_duracion(videos: list[dict]):
    """ Muestra la informacion completa de los datos de la lista de videos formateados
    :params: videos -> lista de tipo diccionario de datos
    :returns: None"""
    
    max_char_tema, max_char_vistas, max_char_durac, max_char_date, max_char_colabs = calcular_tabulacion(videos)    
    for video in videos: 
        
        tema = video.get("Tema")
        duracion = video.get("Duracion")
        
        datos = f'{tema:{max_char_tema}} | {duracion:{max_char_durac + 5}}'
        print(datos)

    
# Quest Lady gaga - Ordenar datos   --------------------------------------------------------

def ordenar_quick_por(videos: list[dict], key: str, modo: str = 'ASC') -> list[dict]:

    if len(videos) < 2:
        return videos
    
    pivot = videos.pop()

    mas_grandes = []
    mas_chicos = []

    for video in videos:
        if video.get(key) > pivot.get(key):
            mas_grandes.append(video)
        else:
            mas_chicos.append(video)
    
    if modo == 'ASC':
        return ordenar_quick_por(mas_chicos, key, modo) + [pivot] + ordenar_quick_por(mas_grandes, key, modo)
    else:
        return ordenar_quick_por(mas_grandes, key, modo) + [pivot] + ordenar_quick_por(mas_chicos, key, modo)

def ordenar_por_duracion(videos: list[dict]):
    """ Ordena los videos por su tiempo de duraciòn en segundos
    Y los muestra.
    :params: videos -> lista de tipo diccionario 
    :returns: None"""

    lista_ordenada = ordenar_quick_por(videos, key='Duracion', modo='DES')
    armar_encabezado('Canciones ordenadas "DES" por tiempo de duracion en segundos: ', videos= lista_ordenada)
    mostrar_videos_completos(lista_ordenada)
    armar_footer(f'Cantidad de reg. grabados: {len(lista_ordenada)}')
    
# Quest Lady gaga - Calcular datos ---------------------------------------------------------

def calcular_promedio(videos: list[dict]) -> float:
    suma = 0
    cantidad = len(videos)

    for video in videos:
        suma += video.get('Vistas')
    
    promedio = suma / cantidad
    return promedio

def mostrar_promedio(videos: list[dict]):
    promedio = calcular_promedio(videos)
    promedio_redondeado = round(promedio / 1000000, 2)

    linea = f'{"-" * 50} \n'
    mensaje = f"El promedio de vistas es: {promedio_redondeado} millones         | \n"
    titulo = f'\n{linea}{mensaje}{linea}\n'
    print(titulo)

def calcular_max_min(videos: list[dict], key:str, operacion: str = 'maximo') -> float:
    """ calcula un maximo o minimo segun parametro """
    max_min = None

    for video in videos:
        if operacion == 'maximo' and (max_min == None or max_min < video.get(key)) or\
            operacion == 'minimo' and (max_min == None or max_min > video.get(key)):
            max_min = video.get(key)

    return max_min

def mostrar_max_min(videos: list[dict], key:str, operacion: str = 'maximo'):
    """ Calcula el valor maximo o minimo que encuentra en una lista.
        y muestra el/los videos que comparten ese valor filtro 
        1 - Accede a una lista de datos de tipo diccionario
        2 - Llama a una funcion que calcuala el minimo/maximo 
        3 - Filtra los videos que igualen ese valor
        4 - Muestra informe de videos filtrados """
    max_min = calcular_max_min(videos, key, operacion)

    mensaje = f'El {operacion} de {key} es {max_min} - Se listan los videos que tienen el {operacion} de vistas: '
    videos_filtrados = filtrar_video(videos= videos, key=key, valor= max_min)
    
    armar_encabezado(mensaje, videos= videos_filtrados) # <- siempre que voy a armar un encabeza, necesito saber cuales datos voy a imprimir
    mostrar_videos_completos(videos_filtrados)          # asi ya ajusto las columnas del encabezado acorde al tamaño de los datos.
    armar_footer(f'Cantidad de reg. grabados: {len(videos_filtrados)}')

# Quest Lady gaga - Filtrar datos ---------------------------------------------------------

def filtrar_video(videos: list[dict], key: str, valor: str) -> list[dict]:
    """ """
    videos_filtrados = []
    for video in videos:
        video_get = video.get(key)
        if valor == video_get:
            videos_filtrados.append(video)
    return videos_filtrados        

def buscar_video_por(videos: list[dict], key: str, valor: str):
    cantidad_maxima_caracteres = max_caracteres(videos, valor=key)
    for video in videos:
        if valor in video.get(key).upper():
            mostrar_info_completa_video(cantidad_maxima_caracteres, video)

def buscar_videos_coincidencia(videos: list[dict], key: str, valor: str) -> list[dict]:
    coincidencias = []

    for video in videos:

        if valor in video.get(key).upper():
            coincidencias.append(video)
    return coincidencias

def mostrar_info_completa(videos: list[dict]):
    cantidad_maxima_caracteres = max_caracteres(videos, valor='Tema')
    for video in videos:
        mostrar_info_completa_video(cantidad_maxima_caracteres, video)

def mostrar_coincidencias(videos: list[dict]):

    buscar_por = input('Buscar por:\nTema\nColaboradores\nOpcion: ').capitalize()
    busqueda = input('Palabra a buscar: ').upper()

    if buscar_por in ('Tema', 'Colaboradores'):
        coincidencias = buscar_videos_coincidencia(videos, key=buscar_por, valor=busqueda)
        armar_encabezado(f'Buscar video por palabra "{buscar_por} - Coincidencia a buscar : "{busqueda}" ', videos= coincidencias)
        mostrar_videos_completos(coincidencias)
        

    else:
        print(f'Error, "{buscar_por}" no es una opcion válida de busqueda')
        mostrar_coincidencias(videos)

def obtener_colaboradores_unicos(videos: list[dict]) -> list[str]:
    """ 1 - Define un set de datos unicos
        2 - por cada videos del diccionario de videos, valida si tiene cargados colaboradores o "No tiene"
        3 - Si tiene colaboradores, los guarda en una lista. Si hay mas de uno aplica .split() y los guarda en un array
        4 - Recorre ese array de colaboradores y los agrega al set [.add()]
        5 - Parse el set a lista
        6 - Ordena la lista 'asc'
        7 - Retorna la lista
        :params: videos -> diccionario de datos
        :returns: lista_colab_unicos -> lista de colaboradores procesados """
    colab_unicos = set()

    for video in videos:
        if not 'No Tiene' in video.get('Colaboradores'):
            colaboradores = video.get('Colaboradores').split(' | ')

            for colaborador in colaboradores:
                colab_unicos.add(colaborador)
    
    lista_colab_unicos = list(colab_unicos)
    lista_colab_unicos.sort()

    return lista_colab_unicos

def mapear_colaboradores(list_colaboradores: list[str]):
    cantidad = len(list_colaboradores)

    for numero in range(cantidad):
        list_colaboradores[numero] = f'{numero + 1} - {list_colaboradores[numero]}'

def mostrar_colaboradores(lista_colab: list[str]):
    for colab in lista_colab:
        print(colab)

def mostrar_videos_con_colab(videos: list[dict]):

    colabs = obtener_colaboradores_unicos(videos)
    # mapear_colaboradores(colabs)

    print('Elija un colaborador de la lista para mostrar un video en le que participe.')
    mostrar_colaboradores(colabs)
    colaborador = input('Escriba un nombre: ').upper()
    coincidencias = buscar_videos_coincidencia(videos, key='Colaboradores', valor=colaborador)
    armar_encabezado('Colaboradores hallados : ', videos= coincidencias)
    mostrar_videos_completos(coincidencias)
    armar_footer(f'\nCantidad de reg grabados: {len(coincidencias)}')
    return coincidencias

def grabar_archivo_salida_colaboradores(ruta_archivo: str, lista_normalizada: list[dict]):
    set_colaboradores = set()
    for cancion in lista_normalizada:
        
        lista_colaboradores = []
        auxiliar = cancion.get('Colaboradores').replace('|', ',')
        lista_colaboradores.append(auxiliar)

        for colaborador in lista_colaboradores:
            lista_aux_colaboradores = list()
            lista_aux_colaboradores = colaborador.split(',')
        
        for i in range(len(lista_aux_colaboradores)):
            set_colaboradores.add(lista_aux_colaboradores[i]) 

    for colaborador in set_colaboradores:

        abrir_escribir_texto(ruta=ruta_archivo, contenido=colaborador, anexar=True)
        print(colaborador)

    print('----------------------------------------------------------')
    print(f'Total colaboradores grabados: {len(set_colaboradores)}')
    print('----------------------------------------------------------')                    
                        

# Quest Lady gaga - Filtrar datos  por mes  ----------------------------------------------------

def mapear_mes(mes: str) -> int:
    """ Recibe una clave  mes y returna su valor correspondiente
    :params: mes -> clave 
    :returns: month_map -> valor dentro del campo mes """
    month_map = {
        'enero' : 1,
        'febrero' : 2,
        'marzo' : 3,
        'abril' : 4,
        'mayo' : 5,
        'junio' : 6,
        'julio' : 7,
        'agosto' : 8,
        'septiembre' : 9,
        'octubre' : 10,
        'noviembre' : 11,
        'diciembre' : 12
    }
    
    return month_map.get(mes, -1)

def mapear_mes_nombre(mes: int) -> str:
    """ Recibe una clave numerica correspondiente al mes y returna su nombre
    :params: mes -> clave numerica 
    :returns: month_map -> nombre en str del mes ingresado como int """
    
    month_map = {
        1 : 'enero',
        2 : 'febrero',
        3 : 'marzo',
        4 : 'abril',
        5 : 'mayo',
        6 : 'junio',
        7 : 'julio',
        8 : 'agosto',
        9 : 'septiembre',
        10 : 'octubre',
        11 : 'noviembre',
        12 : 'diciembre'
    }
    
    return month_map.get(mes, '')

def pedir_mes() ->int:
    """ Pide ingresar un mes al usuario y lo retorna 
    :returns: mes_numero -> numero correspondiente al mes ingresado"""
    mes_nombre = input('Escriba un mes para obtener las canciones lanzadas en dicho mes: ')
    mes_numero = mapear_mes(mes_nombre)
    
    if mes_numero == -1:
        mensaje_error = f'Error. El mes {mes_nombre} ingresado no existe'
        print(mensaje_error)
        mes_numero = pedir_mes()

    return mes_numero

def buscar_videos_coincidencia_mes(videos: list[dict], key: str, valor: int) -> list[dict]:
    """ Recibe un mes numerico y valida que la fecha del video coincida con ese mes valor 
    :params: 
        videos -> dict datos
        key -> clave nombre de campo
        valor -> valor numerico del mes a comparar con la fecha de los registros
    :returns: coinicidencias -> registros hallados
    """
    coincidencias = []

    for video in videos:

        if valor == video.get(key).month:
            coincidencias.append(video)
    return coincidencias

def filtrar_videos_por_mes(videos: list[dict]):                    
    """ Pide al usuario que ingrese un mes y lista los videos lanzados ese mes sin importar el año
    :params: videos -> dict de datos
    :returns: None """
    mes_numerico = pedir_mes()
    coincidencias = buscar_videos_coincidencia_mes(videos= videos,
                                                    key= 'Fecha lanzamiento',
                                                    valor= mes_numerico)
    
    armar_encabezado(f'Lista de videos lanzados en el mes de {mapear_mes_nombre(mes_numerico)} :' , videos= coincidencias)
    mostrar_videos_completos(coincidencias)
    armar_footer(f'Cantidad de reg. grabados: {len(coincidencias)}')




