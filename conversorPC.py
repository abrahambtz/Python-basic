pesos_M = int(input('Cuantos pesos Mexicanos tienes:'))
valor_pesos_C = 0.0054
colombianos = round(pesos_M / valor_pesos_C, 2)
print('Pesos Colombianos: ', colombianos, ' saludos xd')
valor_dolar = 0.00027
dolares = round(colombianos*valor_dolar, 2)
print('Dolares : '+ str(dolares) )


