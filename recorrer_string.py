from typing import runtime_checkable


def run():
    #Recorrer un String 
    # cadena = input('Escribe tu nombre: ')
    # for letra in cadena:
    #     print(letra)
    list = [[1,2,3],[3,2,1]]
    frase = input('Escribe una frase: ')
    for letraMayus in list:
        print(letraMayus)
    i = 0
    while i<1000:
        print(i)
        i+= 1

if __name__ == '__main__':
    run() 