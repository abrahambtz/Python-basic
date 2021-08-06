def run():
    def es_primo(num):
        x = num-10
        for n in range(2, num):
            if num % n == 0:
                print("No es primo", n, "es divisor")
                return False
            print("Es primo"+str(n))
            return True
    primos = int(input("Ingrese el numero:"))
    es_primo(primos)
if __name__ == '__main__':
    run()
