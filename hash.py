def run():

    
    cadena = input('Ingresa la cadena : ')
    

    lista_ascii = [ord(i) for i in cadena]
    
    unir_cadena = ''
    for i in range(len(lista_ascii)):
        unir_cadena = unir_cadena + str(lista_ascii[i])
   
    list_pares = []
    longitud_cadena = len(unir_cadena)
    cont = 0
    reducir = longitud_cadena
    while cont < longitud_cadena:
        reducir = reducir - 2
        if(reducir < 0):
            par = unir_cadena[cont]
            list_pares.append(par)
        else:
            par = unir_cadena[cont] + unir_cadena[cont+1]
            list_pares.append(par)    
        cont = cont + 2
    
    for i in range(longitud_cadena-1, -1, -1):
        if(es_primo(i)):
            primo_cercano = i
            break
   
    longitud_lista_pares = len(list_pares)
    tabla_modular = [[]] * (primo_cercano )
    
    
    for i in range(longitud_lista_pares-1, -1, -1):
        indice =  int(list_pares[i]) % primo_cercano
        #listEx.append(longitud_lista_pares[i])
        tabla_modular[indice] = tabla_modular[indice] +[list_pares[i]]
    print('hola')
    i = 0
    while i < len(tabla_modular):
        if len(tabla_modular[i])>1:
            mover_numero = [tabla_modular[i][-1]]
            for j in range(len(tabla_modular)):
                if len(tabla_modular[j])<1 :
                    tabla_modular[j] = mover_numero
                    tabla_modular[i] = tabla_modular[i][:-1]
                
        else:
            i= i+1
    lista_a_cadena = ''
    for i in range(len(tabla_modular)):
        if len(tabla_modular[i]) > 0: 
            lista_a_cadena =lista_a_cadena + ''.join(str(tabla_modular[i][0]))
    
    print(lista_a_cadena)
    list_dividida = dividir_en_dos(lista_a_cadena[::-1])
    print(list_dividida)
    
def Hexadecimal(dec):
    x = (decimal % 16)
    digitos = "0123456789ABCDEF"
    resta = decimal / 16
    if (resta == 0):
        return digitos[x]
    return Hexadecimal(resta) + digitos[x]


def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True    
    
def dividir_en_dos(unir_cadena):
  list_pares = []
  longitud_cadena = len(unir_cadena)
  cont = 0
  reducir = longitud_cadena
  while cont < longitud_cadena:
      reducir = reducir - 2
      if(reducir < 0):
          par = unir_cadena[cont]
          list_pares.append(par)
      else:
          par = unir_cadena[cont] + unir_cadena[cont+1]
          list_pares.append(par)    
      cont = cont + 2
  return list_pares

if __name__ == '__main__':
    run()
