#Este es un menu donde py puede leer todo el texto utilizando 3 comillas
menu = """

Bienvenido al conversor de monedas.

------------------------------------

* Opcion 1 : Convertir de pesos mexicanos a dolares.
* Opcion 2 : Convertir de pesos colombianos a dolares.
* Opcion 3 : Convertir de dolares a pesos mexicanos.
* Opcion 4 : Convertir de dolares a pesos colombianos.

"""

print(menu)
opt = int(input('Seleccione una opcion.'))
# edad = int(input('Escribe tu edad: '))
# nombre = input('Escribe tu nombre: ')

# print('Hola '+ nombre + ' tu edad es: ' + str(edad))

valorMx = 5
valorC = 10
dolar = 0

if opt == 1:
    monedaMX = float(input('Cuanto pesos mexicanos tienes? : '))
elif opt == 2:
    monedaC = float(input('Cuanto pesos colombianos tienes? : '))
elif opt == 3:
    monedaEUA =  float(input('Cuanto pesos colombianos tienes? : '))
elif opt == 4:
    monedaEUA =  float(input('Cuanto pesos colombianos tienes? : '))
else:
    print('Selecciona una opcion del 1, 2, 3, 4')



# if edad < 18:
#     print('Tu eres menor de edad')
# else:
#     print('Tu eres mayor de edad')
# print('Final del programa')

