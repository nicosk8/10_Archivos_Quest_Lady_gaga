from lady_gaga import playlist_lady_gaga
from application import application
from archivos import crear_archivo_csv

if __name__ == '__main__':

    entrada = crear_archivo_csv(playlist_lady_gaga)
    application(entrada)