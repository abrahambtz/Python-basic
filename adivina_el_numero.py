import random

def run():
    numero_random = random.randint(1, 100)
    numero = int(input('Elige un numero entre 1 a 100: '))
    while numero != numero_random:
        if numero < numero_random:
            print('Selecciona un numero mas grande.')
        else:
            print('Selecciona un numero mas chico.')
        numero = int(input('Ingresa otro numero: '))
    print('Adivinaste el numero')
    

if __name__ == '__main__':
    run()
