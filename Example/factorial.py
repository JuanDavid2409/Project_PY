def main():
    cantidad = if_entero()
    lista = []
    
    for i in range(cantidad):
        numero = int(input("Ingrese numero: "))
        lista.append(numero)
        
    res = factorial(lista)
    
    print(res)
    
def factorial(number):
    return sum(number)

def if_entero():
    while True:
        entero = input("Ingrese cantidad de numeros: ")
        try:
            entero = int(entero)
            return entero
        except ValueError:
            print("No es un numero")

if __name__ == "__main__":
    main()