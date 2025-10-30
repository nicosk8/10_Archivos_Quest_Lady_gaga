import copy 
import datetime
from menu import show_menu
from validations import validate_input
import os
import functions as fun
from archivos import (
    CSV_CANCIONES_LADYGAGA, cargar_datos_a_diccionario_desde_archivo,JSON_FILE_CANCIONES_LADY_GAGA, abrir_grabar_archivo_json
)


def application(archivo_entrada):
    
    running = True
    lista_normalizada = []
 
    while running:
        show_menu()
        option = validate_input(0, 10)
        print()

        match option:
            case 0:
                lista_registros_entrada = cargar_datos_a_diccionario_desde_archivo(CSV_CANCIONES_LADYGAGA)
                cantidad_impresos = 0
                for diccionario in lista_registros_entrada:
                    for clave, valor in diccionario.items():
                        print(f'{clave} : {valor}')
                    print()
                    cantidad_impresos += 1
                print('-----------------------------------------------------------------------------------')
                print(f'Total impresos: {cantidad_impresos}')
                print('-----------------------------------------------------------------------------------\n\n')
    
            case 1:
                                
                lista_normalizada = fun.normalizar_datos(lista_registros_entrada)            
                fun.armar_encabezado('| Datos normalizados para procesar', videos= lista_normalizada)
                fun.mostrar_videos_completos(lista_normalizada)
                fun.armar_footer(f'Cantidad de reg. grabados: {len(lista_normalizada)}')

                # aca tendria que guardar los datos de lista_normalizada en un archivo JSON
                # crear JSON, abrirlo en modo w y a (append), grabarlo, cerrarlo.
                
                for cancion in lista_normalizada: # <- formateo la fecha a str
                    cancion['Fecha lanzamiento'] = diccionario['Fecha lanzamiento'].strftime("%Y-%m-%d")

                abrir_grabar_archivo_json(JSON_FILE_CANCIONES_LADY_GAGA, modo = 'w', contenido= lista_normalizada, clave='canciones')
                

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
