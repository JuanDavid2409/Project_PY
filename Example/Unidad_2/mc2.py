def main():
    #Masa en KG
    masa = if_numero() #int(input("Ingrese la masa en kg: "))

    #Ecuacion e=mc2
    c = 300000
    energia = masa * c * c
    
    print("El calculo de la ecuacion es: " + energia)

def if_numero():
    while True:
        numero=input("Ingrese la masa en kg: ")
        try:
            numero=int(numero)
            return numero
        except ValueError:
            print("No es un numero")
            
if __name__ == "__main__":
    main()