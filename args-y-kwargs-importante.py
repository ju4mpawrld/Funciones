#  En Python, args y kwargs son convenciones comunes para nombrar parámetros que permiten que una función reciba un número variable de argumentos y palabras clave.

# *args permite pasar un número variable de argumentos posicionales (como tuplas) a una función. Dentro de la función, args se comporta como una tupla que contiene todos los argumentos posicionales pasados.

# Por ejemplo, el siguiente código define una función que toma un número variable de argumentos posicionales y los suma:

# arduino
# Copy code
# def sumar(*args):
#     total = 0
#     for numero in args:
#         total += numero
#     return total
# La función sumar puede ser llamada con cualquier cantidad de argumentos, y todos los argumentos serán sumados:

# python
# Copy code
# >>> sumar(1, 2, 3)
# 6
# >>> sumar(4, 5, 6, 7)
# 22
# Por otro lado, **kwargs permite pasar un número variable de argumentos de palabras clave (como diccionarios) a una función. Dentro de la función, kwargs se comporta como un diccionario que contiene todas las palabras clave y sus valores.

# Por ejemplo, el siguiente código define una función que toma un número variable de argumentos de palabras clave y los imprime:

# python
# Copy code
# def imprimir_parametros(**kwargs):
#     for parametro, valor in kwargs.items():
#         print(f"{parametro}: {valor}")
# La función imprimir_parametros puede ser llamada con cualquier cantidad de argumentos de palabras clave, y todos los argumentos serán impresos:

# makefile
# Copy code
# >>> imprimir_parametros(nombre="Juan", edad=30, ciudad="Bogotá")
# nombre: Juan
# edad: 30
# ciudad: Bogotá
# Es importante destacar que args y kwargs son solo convenciones de nombres, y puedes usar cualquier otro nombre que desees para tus parámetros. Lo importante es que entiendas cómo funcionan y cómo usarlos en tus programas.
