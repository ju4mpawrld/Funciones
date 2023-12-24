def suma(*numeros):  # CON EL ASTERISCO LE INDICAMOS QUE ESTO SE VA A TRATAR DE ALGO ITERABLE
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5)
suma(2, 5, 7, 6)  # TODOS ESTOS SE ASIGNAN AL PARAMETRO DE NUMEROS
suma(2, 4, 44, 33)
