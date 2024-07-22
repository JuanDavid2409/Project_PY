#Calcular la media de una lista de numeros, mostrar los numeros ingresados, sumar y dividir por la cantidad
def main():
    cantidad = entero()
    lista_numeros = []

    for i in range(cantidad):
        number = int(input("Ingrese un numero: "))
        lista_numeros.append(number)

        res = media(lista_numeros)
            
    print("La media de los numeros " + " ".join(str(lista_numeros)) + " es: " + str(res))

def media(numeros):
    return sum(numeros)/len(numeros)

def entero():
    while True:
        entrada = input("Ingrese cantidad de numeros: ")
        try:
            entrada = int(entrada)
            return entrada
        except ValueError:
            print("No es un numero, intente de nuevo")
            
            

if __name__ == "__main__":
    main()