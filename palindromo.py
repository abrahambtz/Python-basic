palabra = input('Escribe una palabra: ')
def palindromo(palabra_validar):
    if palabra_validar == palabra_validar[::-1]:
        print('Es palindromo')
    else:
        print('No es palindromo')

palindromo(palabra.replace(' ','').lower())



