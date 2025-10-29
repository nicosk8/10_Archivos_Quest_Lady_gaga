import copy 
from menu import show_menu
from validations import validate_input
import os
import functions as fun
from archivos import (
    CSV_CANCIONES_LADYGAGA, cargar_datos_desde_archivo
)


def application(archivo_entrada):
    
    running = True
    lista_normalizada = []
 
    while running:
        show_menu()
        option = validate_input(0, 10)
#        lista_registros_entrada = cargar_datos_desde_archivo(CSV_CANCIONES_LADYGAGA)

        match option:
            case 0:
                lista_registros_entrada = cargar_datos_desde_archivo(CSV_CANCIONES_LADYGAGA)
                for reg in lista_registros_entrada: # imprimo la lista[str] que carguè
                    print(reg)

            case 1:
                
                diccionario_canciones = {} # ahora tengo que hacer a la inversa
                                           # tengo que armar un diccionario de datos desde un .csv 
                                           # y lo tengo que recibir acà
                
                lista_normalizada = fun.normalizar_datos(diccionario_canciones)
#                

                fun.armar_encabezado('| Datos normalizados para procesar', videos= lista_normalizada)
                fun.mostrar_videos_completos(lista_normalizada)
                fun.armar_footer(f'Cantidad de reg. grabados: {len(lista_normalizada)}')

            case 2:

                fun.armar_encabezado_titulo_duracion('| Lista de videos: ', videos= lista_normalizada)
                fun.mostrar_videos_completos_titulo_duracion(lista_normalizada)
                fun.armar_footer(f'Cantidad de reg. grabados: {len(lista_normalizada)}')

            case 3:
                fun.ordenar_por_duracion(lista_normalizada)
            case 4:
                fun.mostrar_promedio(lista_normalizada)
            case 5:
                fun.mostrar_max_min(lista_normalizada, key='Vistas', operacion='maximo')
            case 6:
                fun.mostrar_max_min(lista_normalizada, key='Vistas', operacion='minimo')
            case 7:
                fun.mostrar_coincidencias(lista_normalizada)
            case 8:
                fun.mostrar_videos_con_colab(lista_normalizada)
            case 9:
                fun.filtrar_videos_por_mes(lista_normalizada)
            case 10:
                running = False
                print('Cerrando App')
        os.system('pause')
        os.system('cls')
