menu = """
Bienvenido al conversor de monedas.

------------------------------------

* Opcion 1 : Convertir de pesos mexicanos a colombianos
* Opcion 2 : Convertir de pesos mexicanos a dolares.
* Opcion 3 : Convertir de dolares a pesos mexicanos.

Selecciona una opcion: 
"""
def convertidor(tipo_moneda, moneda_a_convertir):
    moneda= float(input('Cuantos ' + tipo_moneda + ' tienes?: '))
    moneda_convertida = (moneda * moneda_a_convertir)
    return moneda_convertida

opc = int(input(menu))

tex_pesos_mexicanos = 'pesos mexicanos'
tex_dolar = 'dolares'

valor_colombiano = 186.93 
valor_dolar = 0.050 
valor_mexicano =  19.95

if opc == 1:
    moneda_convertida = convertidor(tex_pesos_mexicanos, valor_colombiano)
    print('Su conversion a pesos colombianos es de: ', moneda_convertida)
elif opc == 2:
    moneda_convertida = convertidor(tex_pesos_mexicanos, valor_dolar)
    print('Su conversion a dolares es de: ', moneda_convertida)
elif opc == 3:
    moneda_convertida = convertidor(tex_dolar, valor_mexicano)
    print('Su conversion a pesos mexicanos es de: ', moneda_convertida)
