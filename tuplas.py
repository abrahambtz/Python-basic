def run():
    tuplas = (1,2,3,3)
    print(tuplas)
    # Las tuplas son listas constantes, no se pueden modificar.
    #Esto quiere decir que son estaticas

    for item in tuplas:
        print(item)
if __name__ == '__main__':
    run()