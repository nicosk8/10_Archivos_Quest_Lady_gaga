import copy 
from menu import show_menu
from validations import validate_input
import os
import functions as fun

def application(songs: list[dict]):
    
    running = True
    lista_normalizada = []

    while running:
        show_menu()
        option = validate_input(1, 10)

        match option:
            case 1:
                
                lista_normalizada = fun.normalizar_datos(songs)
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
