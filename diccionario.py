def run():
    diccionario = {
        'key1': 1,
        'key2': 2,
        'key3': 3
    }
    print('Aceder a elementos del diccionario: ',diccionario['key1'])
    print('Diccionario completo: ')
    print(diccionario)
    #Imprimir sololas llaves
    for key in diccionario.keys():
        print(key)

    #Imprimir solo los valores.
    for value in diccionario.values():
        print(value)
    #Imprimir las llaves y los valores.
    for key, value in diccionario.items():
        print('La llave es ' + key + ' y su valor es: ' + str(value))

if __name__ == '__main__':
    run()