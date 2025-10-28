"""
Creación y Acceso Básico
Ejercicio: Crea un diccionario llamado informacion_personal con las claves: "nombre", "edad", "ciudad", y "ocupación". Asigna valores apropiados. Luego, imprime el valor de la clave "edad".

2. Agregar y Modificar Elementos
Ejercicio: Usando el diccionario informacion_personal del ejercicio anterior, agrega una nueva clave llamada "email" con un correo ficticio. Después, cambia el valor de la clave "ciudad" a "Córdoba". Imprime el diccionario completo.

3. Eliminar Elementos (usando del)
Ejercicio: Crea un diccionario llamado frutas con al menos tres frutas y sus precios. Luego, usa la palabra clave del para eliminar una de las frutas y su precio. Imprime el diccionario antes y después de la eliminación.

4. Iterar sobre Claves y Valores
Ejercicio: Itera sobre el siguiente diccionario capitales e imprime cada par clave-valor en el formato: "La capital de [País] es [Capital]".
capitales = { "Japón": "Tokio","Francia": "París", "Canadá": "Ottawa" }

5. Obtener Claves, Valores y Pares (keys(), values(), items())
Ejercicio: Dado el diccionario colores, imprime por separado una lista de todas las claves, una lista de todos los valores y, por último, la representación de todos los pares clave-valor.
colores = { "rojo": "#FF0000", "verde": "#00FF00", "azul": "#0000FF" }

6. Uso de get() para Evitar Errores
Ejercicio: Intenta acceder a una clave que no existe en el diccionario configuración de dos maneras: configuración = {"tema": "oscuro", "fuente": "Arial"}
Directamente con corchetes ([]). (Esto debería causar un error si no lo manejas).
Usando el método .get(), proporcionando un valor predeterminado (default) de "No configurado".

7. Contar Frecuencias con un Diccionario
Ejercicio: Dada la siguiente lista de palabras, usa un diccionario para contar y almacenar la frecuencia de cada palabra (cuántas veces aparece).
palabras = ["gato", "perro", "gato", "pez", "perro", "gato"]

8. Diccionario Anidado (Nested Dictionary)
Ejercicio: Crea un diccionario llamado estudiantes donde cada clave sea un nombre y su valor sea otro diccionario con las claves "matematicas" e "programación 1" con las notas de ese estudiante. Imprime la nota de matemáticas de "Pepe" (Debe ser una de las claves de tu diccionario).

9. Actualizar Diccionarios con update()
Ejercicio: Tienes un diccionario base usuario_perfil y un diccionario de nuevas configuraciones nuevas_preferencias. Usa el método .update() para fusionar las nuevas preferencias en el perfil del usuario.
usuario_perfil = {"nombre": "Leo", "tema": "claro", "notificaciones": True} nuevas_preferencias = {"tema": "oscuro", "sonido": False}

10. pop() para Extraer y Eliminar
Ejercicio: Usa el método .pop() para obtener y eliminar la clave "puerto" del diccionario servidor. Imprime el valor extraído y luego el diccionario restante.
servidor = { "ip": "192.168.1.1", "puerto": 8080, "estado": "activo" }
"""

"""
1 - Creación y Acceso Básico
Ejercicio: Crea un diccionario llamado informacion_personal con 
las claves: "nombre", "edad", "ciudad", y "ocupación". 
Asigna valores apropiados. Luego, imprime el valor de la clave "edad".
"""
informacion_personal = {
    "nombre": 'Pepe',
    "edad": 56,
    "ciudad": 'Boedo',
    "ocupacion": 'Vendedor'
}

# print(informacion_personal.get('edad', 'No se encontro la clave'))

"""
2. Agregar y Modificar Elementos
Ejercicio: Usando el diccionario informacion_personal 
del ejercicio anterior, agrega una nueva clave llamada 
"email" con un correo ficticio. Después, cambia el valor 
de la clave "ciudad" a "Córdoba". Imprime el diccionario completo.
"""

informacion_personal['email'] = 'pepe@vendedor.com'
informacion_personal['ciudad'] = 'Cordoba'
# print(informacion_personal)

"""
3. Eliminar Elementos (usando del)
Ejercicio: Crea un diccionario llamado frutas con 
al menos tres frutas y sus precios. Luego, usa la 
palabra clave del para eliminar una de las frutas y su precio. 
Imprime el diccionario antes y después de la eliminación.

"""

frutas = {
    "manzana": 1500,
    "naranja": 1250,
    "palta": 5000
}

# print(frutas)

# del frutas['manzana']

# print(frutas)

"""
4. Iterar sobre Claves y Valores
Ejercicio: Itera sobre el siguiente diccionario capitales e 
imprime cada par clave-valor en el formato: 
"La capital de [País] es [Capital]".
capitales = { "Japón": "Tokio","Francia": "París", "Canadá": "Ottawa" }

"""

capitales = { "Japón": "Tokio","Francia": "París", "Canadá": "Ottawa" }

# for pais, capital in capitales.items():
#     mensaje = f"La capital de {pais} es {capital}"
#     print(mensaje)

"""
5. Obtener Claves, Valores y Pares (keys(), values(), items())
Ejercicio: Dado el diccionario colores, 
imprime por separado una lista de todas las claves, 
una lista de todos los valores y, por último, la 
representación de todos los pares clave-valor.
colores = { "rojo": "#FF0000", "verde": "#00FF00", "azul": "#0000FF" }

"""
colores = { "rojo": "#FF0000", "verde": "#00FF00", "azul": "#0000FF" }

# for color in colores.keys():
#     print(color)

# for valor_hexa in colores.values():
#     print(valor_hexa)

# for color, valor_hexa in colores.items():
#     print(color, valor_hexa)

"""
6. Uso de get() para Evitar Errores
Ejercicio: Intenta acceder a una clave que no existe en el diccionario 
configuración de dos maneras: configuración = {"tema": "oscuro", "fuente": "Arial"}
Directamente con corchetes ([]). (Esto debería causar un error si no lo manejas).
Usando el método .get(), proporcionando un valor predeterminado (default) de "No configurado".
"""
configuración = {"tema": "oscuro", "fuente": "Arial"}

# clave_falsa_1 = configuración.get('font_size', 'No existe la clave font_size')
# print(clave_falsa_1)
# clave_falsa_2 = configuración['font_size']
# print(clave_falsa_2)

"""
7. Contar Frecuencias con un Diccionario
Ejercicio: Dada la siguiente lista de palabras, usa un diccionario 
para contar y almacenar la frecuencia de cada palabra (cuántas veces aparece).
palabras = ["gato", "perro", "gato", "pez", "perro", "gato"]
"""
palabras = ["gato", "perro", "gato", "pez", "perro", "gato"]
frecuencias = {}

"""
frecuencias = {
    "gato": 3,
    "perro": 2,
    "pez": 1
}
"""

for palabra in palabras:
    # if not palabra in frecuencias.keys():
    #     frecuencias[palabra] = 1
    # else:
    #     frecuencias[palabra] = frecuencias.get(palabra) + 1
 
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

# print(frecuencias)

"""
8. Diccionario Anidado (Nested Dictionary)
Ejercicio: Crea un diccionario llamado estudiantes 
donde cada clave sea un nombre y su valor sea otro 
diccionario con las claves "matematicas" e "programación 1" 
con las notas de ese estudiante. Imprime la nota de matemáticas 
de "Pepe" (Debe ser una de las claves de tu diccionario).

"""

estudiantes = {
    "Pepe": {
        "matematicas": 5,
        "programacion 1": 5
    },
    "Moni": {
        "matematicas": 3,
        "programacion 1": 3
    },
    "Paola": {
        "matematicas": 2,
        "programacion 1": 2
    }
}

notas_pepe = estudiantes.get('Pepe')
nota_mate_pepe = notas_pepe.get('matematicas')
# print(nota_mate_pepe)


# for estudiante, notas in estudiantes.items():
#     print(f'Notas de {estudiante}:')
#     for materia, nota in notas.items():
#         print(f'    {materia}: {nota}')

"""
9. Actualizar Diccionarios con update()
Ejercicio: Tienes un diccionario base usuario_perfil y un 
diccionario de nuevas configuraciones nuevas_preferencias. 
Usa el método .update() para fusionar las nuevas preferencias en el perfil del usuario.
usuario_perfil = {"nombre": "Leo", "tema": "claro", "notificaciones": True} 
nuevas_preferencias = {"tema": "oscuro", "sonido": False}
"""
usuario_perfil = {"nombre": "Leo", "tema": "claro", "notificaciones": True} 
nuevas_preferencias = {"tema": "oscuro", "sonido": False}

usuario_perfil.update(nuevas_preferencias)
# print(usuario_perfil)

"""
10. pop() para Extraer y Eliminar
Ejercicio: Usa el método .pop() para obtener y eliminar la 
clave "puerto" del diccionario servidor. Imprime el valor extraído y luego el diccionario restante.
servidor = { "ip": "192.168.1.1", "puerto": 8080, "estado": "activo" }
"""
servidor = { "ip": "192.168.1.1", "puerto": 8080, "estado": "activo" }

# print(servidor)

# puerto = servidor.pop('puerto')
# print(f'El puerto eliminado es: {puerto}')

# print(servidor)


texto = "Alcides - Hold My Hand (Top Gun: Maverick)"
elementos_texto = texto.split(' - ')
# print(elementos_texto)

nombre_tema = ''
colaboradores = 'No tiene'

if len(elementos_texto) > 1:
    colaboradores = elementos_texto[0]
    nombre_tema = elementos_texto[1]
else:
    nombre_tema = elementos_texto[0]

print(nombre_tema)
print(colaboradores)