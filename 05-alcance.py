# saludo = "hola global"  # alcance global, que no se deberia ocupar.


def saludar():
    saludo = "holaaa"  # alcance local de la función saludar
    print(
        saludo
    )  # aquí solo puedo acceder a la variable 'saludo' desde dentro de la función


def saludachanchito():  # alcance local de la función saludachanchito
    saludo = "hola chanchito"  # la misma variable de arriba pero en otro contexto, son distintas
    print(saludo)


saludar()
# print(saludo)  # Accedemos a la variable 'saludo' con alcance global
animal = "el pepe"
palabra_al_reves = animal[::-1]
print(palabra_al_reves)
